"""Deterministic, study-level TrialTrace feasibility prototype."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

LABEL_TO_DIRECTION = {
    "significantly decreased": "DECREASED",
    "no significant difference": "NO_DIFFERENCE",
    "significantly increased": "INCREASED",
}


@dataclass(frozen=True)
class EvidenceUnit:
    evidence_id: str
    text: str
    start: int | None
    end: int | None
    annotation_id: str


@dataclass(frozen=True)
class TrialTraceInstance:
    instance_id: str
    question_id: str
    question: str
    review_id: str | None
    trial_family_id: str | None
    report_id: str
    article_id: str
    pico: dict[str, str]
    outcome_identity: str
    effect_direction: str
    evidence_spans: tuple[EvidenceUnit, ...]
    provenance: dict[str, Any]
    evidence_set: tuple[str, ...]
    perturbation: dict[str, Any]
    expected_decision: str


def stable_id(payload: Any) -> str:
    """Return a version-stable SHA-256 identifier for JSON-compatible data."""
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(encoded).hexdigest()


def _as_int(value: str) -> int | None:
    try:
        result = int(value)
    except (TypeError, ValueError):
        return None
    return result if result >= 0 else None


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_clean_instances(root: Path, limit: int | None = None) -> list[dict[str, Any]]:
    """Build valid, one-report EI instances without inventing trial links."""
    annotations = _read_rows(root / "annotations_merged.csv")
    prompts = {row["PromptID"]: row for row in _read_rows(root / "prompts_merged.csv")}
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in annotations:
        if row.get("Valid Label", "").lower() == "true" and row.get("Label") in LABEL_TO_DIRECTION:
            grouped[row["PromptID"]].append(row)

    instances: list[dict[str, Any]] = []
    for prompt_id in sorted(grouped, key=lambda value: int(value)):
        prompt = prompts.get(prompt_id)
        rows = grouped[prompt_id]
        if prompt is None or not prompt.get("PMCID"):
            continue
        counts = Counter(row["Label"] for row in rows)
        label = min(counts, key=lambda value: (-counts[value], value))
        spans: list[dict[str, Any]] = []
        for index, row in enumerate(rows):
            start, end = _as_int(row.get("Evidence Start", "")), _as_int(row.get("Evidence End", ""))
            if start is not None and end is not None and end >= start:
                evidence_payload = {"prompt_id": prompt_id, "annotation": index, "start": start, "end": end}
                spans.append({
                    "evidence_id": stable_id(evidence_payload),
                    "text": row.get("Annotations", ""),
                    "start": start,
                    "end": end,
                    "annotation_id": f"{prompt_id}:{index}",
                })
        base = {
            "question_id": f"ei2:{prompt_id}",
            "question": f"With respect to {prompt['Outcome']}, characterize the reported difference between {prompt['Intervention']} and {prompt['Comparator']}.",
            "review_id": None,
            "trial_family_id": None,
            "report_id": f"pmcid:{prompt['PMCID']}",
            "article_id": f"PMCID:{prompt['PMCID']}",
            "pico": {"population": "", "intervention": prompt["Intervention"], "comparator": prompt["Comparator"]},
            "outcome_identity": prompt["Outcome"],
            "effect_direction": LABEL_TO_DIRECTION[label],
            "evidence_spans": spans,
            "provenance": {
                "source": "Evidence Inference 2.0",
                "prompt_id": prompt_id,
                "pmcid": prompt["PMCID"],
                "raw_annotation_count": len(rows),
                "label_rule": "majority over valid annotations; lexical tie-break",
            },
            "evidence_set": [f"pmcid:{prompt['PMCID']}"],
            "perturbation": {"type": "CLEAN", "seed": None, "parent_instance_id": None},
            "expected_decision": "SYNTHESIZE",
        }
        base["instance_id"] = stable_id(base)
        instances.append(base)
        if limit is not None and len(instances) >= limit:
            break
    return instances


def random_omission(instance: dict[str, Any], seed: int) -> dict[str, Any]:
    """Remove the sole report; this is valid only as an abstention feasibility probe."""
    output = json.loads(json.dumps(instance))
    output["evidence_set"] = []
    output["evidence_spans"] = []
    output["perturbation"] = {
        "type": "RANDOM_EVIDENCE_OMISSION",
        "seed": seed,
        "parent_instance_id": instance["instance_id"],
        "removed_report_ids": [instance["report_id"]],
        "rule": "remove the sole available report",
        "semantic_consequence": "evidence insufficiency under the prototype contract",
    }
    output["expected_decision"] = "ABSTAIN"
    output["instance_id"] = stable_id({k: v for k, v in output.items() if k != "instance_id"})
    return output


def generate_prototype(root: Path, output: Path, limit: int = 64, seed: int = 17) -> dict[str, Any]:
    clean = build_clean_instances(root, limit=limit)
    perturbed = [random_omission(item, seed + index) for index, item in enumerate(clean)]
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="\n") as handle:
        for item in clean + perturbed:
            handle.write(json.dumps(item, sort_keys=True, ensure_ascii=False) + "\n")
    return {"clean_count": len(clean), "omission_count": len(perturbed), "total_count": len(clean) + len(perturbed), "seed": seed}


def heuristic_sanity(path: Path) -> dict[str, Any]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    predictions = ["SYNTHESIZE" if row["evidence_set"] else "ABSTAIN" for row in rows]
    truth = [row["expected_decision"] for row in rows]
    accuracy = sum(p == y for p, y in zip(predictions, truth)) / len(truth) if truth else 0.0
    return {"n": len(rows), "evidence_count_rule_accuracy": accuracy, "warning": "prototype labels make omission answerability directly observable"}


def source_manifest(paths: list[Path], output: Path) -> None:
    records = []
    for path in sorted(paths):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        records.append({"path": str(path), "bytes": path.stat().st_size, "sha256": digest})
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"files": records}, indent=2) + "\n", encoding="utf-8")
