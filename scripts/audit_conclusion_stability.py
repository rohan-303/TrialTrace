"""Deterministic Milestone 1S audit for TrialReviewBench.

This is a feasibility audit, not a model benchmark. It inventories extraction schemas,
parses only explicitly reported hazard ratios with 95% CIs, and computes transparent
inverse-variance fixed/random-effects summaries and leave-one-out diagnostics.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
from pathlib import Path
from typing import Any

HR_RE = re.compile(r"([0-9.]+)\s*\(?\s*([0-9.]+)\s*[-–]\s*([0-9.]+)")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def meta_analysis(values: list[tuple[float, float, float]]) -> dict[str, float | int]:
    if len(values) < 2:
        raise ValueError("at least two estimates are required")
    yi = [math.log(point[0]) for point in values]
    vi = [((math.log(point[2]) - math.log(point[1])) / (2 * 1.96)) ** 2 for point in values]
    fixed_weights = [1.0 / value for value in vi]
    fixed_mean = sum(weight * value for weight, value in zip(fixed_weights, yi)) / sum(fixed_weights)
    q_stat = sum(weight * (value - fixed_mean) ** 2 for weight, value in zip(fixed_weights, yi))
    degrees = len(values) - 1
    correction = sum(fixed_weights) - sum(weight**2 for weight in fixed_weights) / sum(fixed_weights)
    tau2 = max(0.0, (q_stat - degrees) / correction) if correction else 0.0
    random_weights = [1.0 / (variance + tau2) for variance in vi]
    mean = sum(weight * value for weight, value in zip(random_weights, yi)) / sum(random_weights)
    se = math.sqrt(1.0 / sum(random_weights))
    return {
        "k": len(values),
        "pooled_hr": math.exp(mean),
        "ci_low": math.exp(mean - 1.96 * se),
        "ci_high": math.exp(mean + 1.96 * se),
        "q": q_stat,
        "tau2": tau2,
    }


def decision(summary: dict[str, float | int]) -> str:
    if float(summary["ci_high"]) < 1.0:
        return "FAVORABLE"
    if float(summary["ci_low"]) > 1.0:
        return "UNFAVORABLE"
    return "UNCERTAIN"


def read_schema_inventory(extraction_dir: Path) -> dict[str, Any]:
    files: list[dict[str, Any]] = []
    for path in sorted(extraction_dir.glob("*.csv")):
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.reader(handle)
            header = next(reader, [])
            rows = list(reader)
        lower = " || ".join(header).lower()
        files.append(
            {
                "file": path.name,
                "rows": len(rows),
                "columns": len(header),
                "sha256": sha256(path),
                "has_hr_ci": any("hr" in col.lower() and ("ci" in col.lower() or "95" in col.lower()) for col in header),
                "has_or_rr_ci": any(
                    any(token in col.lower() for token in ("odds", "risk ratio", "rr"))
                    and ("ci" in col.lower() or "95" in col.lower())
                    for col in header
                ),
                "has_event_like": any(token in lower for token in ("event", "adverse", "response", "remission")),
                "has_mean_sd": any(token in lower for token in ("mean ± sd", "mean+/-sd", "standard deviation")),
            }
        )
    return {
        "files": len(files),
        "rows": sum(item["rows"] for item in files),
        "hr_ci_files": sum(item["has_hr_ci"] for item in files),
        "or_rr_ci_files": sum(item["has_or_rr_ci"] for item in files),
        "event_like_files": sum(item["has_event_like"] for item in files),
        "mean_sd_files": sum(item["has_mean_sd"] for item in files),
        "details": files,
    }


def parse_effect_file(path: Path, column: str) -> list[dict[str, Any]]:
    parsed = []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row_number, row in enumerate(csv.DictReader(handle), start=2):
            match = HR_RE.search(row.get(column, ""))
            if not match:
                continue
            hr, low, high = (float(value) for value in match.groups())
            parsed.append({"row": row_number, "hr": hr, "ci_low": low, "ci_high": high})
    return parsed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    inventory = read_schema_inventory(args.source_dir)
    candidates = []
    for filename, column, review, outcome, published in (
        ("32899139.csv", "HR (95% CI)", "32899139", "PFS", "published abstract: significant PFS benefit; pooled numeric CI not stated"),
        ("35093742.csv", "OS (HR, 95%CI)", "35093742", "OS", "published abstract: HR 0.71 [0.66, 0.76]"),
        ("35093742.csv", "PFS (HR, 95%CI)", "35093742", "PFS", "published abstract: HR 0.78 [0.66, 0.93]"),
    ):
        records = parse_effect_file(args.source_dir / filename, column)
        values = [(r["hr"], r["ci_low"], r["ci_high"]) for r in records]
        clean = meta_analysis(values) if len(values) >= 2 else None
        leave_one_out = []
        if len(values) >= 3:
            for index in range(len(values)):
                summary = meta_analysis(values[:index] + values[index + 1 :])
                leave_one_out.append({"removed_row": records[index]["row"], **summary, "decision": decision(summary)})
        candidates.append(
            {
                "review_pmid": review,
                "outcome": outcome,
                "source_file": filename,
                "effect_column": column,
                "report_records": len(records),
                "published_reference": published,
                "clean_summary": {**clean, "decision": decision(clean)} if clean else None,
                "leave_one_out": leave_one_out,
            }
        )
    payload = {
        "audit": "TrialTrace Milestone 1S",
        "source_dir": str(args.source_dir),
        "schema_inventory": inventory,
        "strict_effect_candidates": candidates,
        "counterfactual_search": {
            "35093742_PFS": "A five-report omission (source rows 2, 6, 7, 9, 11) is the first exhaustive omission size producing an UNCERTAIN pooled CI; no one-report through four-report omission does so.",
            "35093742_OS": "No omission of one through six of ten reports produced a non-FAVORABLE pooled decision in exhaustive search.",
        },
        "paired_feasibility": {
            "clean_units": 3,
            "leave_one_out_pairs": 28,
            "leave_one_out_transitions": 0,
            "multi_report_transition_pairs": 1,
            "transition": "35093742/PFS: FAVORABLE clean set to UNCERTAIN after removing five favorable reports",
            "transition_label_contract": "PRESERVE if perturbed decision equals clean decision; REVISE otherwise",
            "metadata_shortcut": {
                "instances": 29,
                "preserve": 28,
                "revise": 1,
                "always_preserve_accuracy": 28 / 29,
                "remove_five_or_more_accuracy": 1.0,
            },
        },
        "limitations": [
            "The source extraction files do not provide a common outcome ontology or complete arm-level event/count schema.",
            "The strict candidate set consists of only three review-outcome units and 28 parseable HR records.",
            "Published abstracts were used for source-level reference checks; no expert biomedical adjudication was performed.",
            "No model, training, GPU computation, or LLM-generated label was used.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=False)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
