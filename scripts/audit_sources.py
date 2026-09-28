from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    repo = Path(__file__).resolve().parents[1]
    ei = repo / "data/interim/evidence_inference_v2"
    ms2 = json.loads((repo / "data/raw/ms2/sample.json").read_text(encoding="utf-8"))
    ann = csv_rows(ei / "annotations_merged.csv")
    prompts = csv_rows(ei / "prompts_merged.csv")
    valid = [row for row in ann if row.get("Valid Label", "").lower() == "true"]
    split_sets = {}
    for name in ("train_article_ids.txt", "validation_article_ids.txt", "test_article_ids.txt"):
        split_sets[name] = {line.strip() for line in (ei / "splits" / name).read_text().splitlines() if line.strip()}
    split_intersections = {
        f"{a}__{b}": len(split_sets[a] & split_sets[b])
        for a, b in (("train_article_ids.txt", "validation_article_ids.txt"), ("train_article_ids.txt", "test_article_ids.txt"), ("validation_article_ids.txt", "test_article_ids.txt"))
    }
    proto_path = repo / "data/processed/prototype/trialtrace_prototype_v0_1.jsonl"
    proto = [json.loads(line) for line in proto_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    manifest_paths = [
        repo / "data/raw/ms2/sample.json",
        repo / "data/raw/ms2/README.md",
        repo / "data/raw/evidence_inference/README.md",
        repo / "data/raw/evidence_inference/README.annotation_process.md",
        repo / "data/raw/evidence_inference/v2.0.tar.gz",
        ei / "annotations_merged.csv",
        ei / "prompts_merged.csv",
    ]
    manifest = {
        "retrieval_date": "2026-09-28",
        "sources": [
            {"name": "MS2 sample", "url": "https://raw.githubusercontent.com/allenai/ms2/master/sample.json", "license_reference": "https://github.com/allenai/ms2/blob/master/README.md"},
            {"name": "Evidence Inference 2.0", "url": "https://evidence-inference.ebm-nlp.com/v2.0.tar.gz", "license_reference": "https://github.com/jayded/evidence-inference/blob/master/LICENSE"},
        ],
        "files": [{"path": str(path.relative_to(repo)).replace("\\", "/"), "bytes": path.stat().st_size, "sha256": sha256(path), "git_tracked": False} for path in manifest_paths],
        "raw_data_policy": "raw and derived clinical text are excluded from Git; compact manifests and code may be committed",
    }
    (repo / "data/manifests/milestone_1_source_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    stats = {
        "ms2_sample": {
            "review_count": 1,
            "included_study_groups": len(ms2.get("included_studies", [])),
            "included_reports": sum(len(group.get("references", [])) for group in ms2.get("included_studies", [])),
            "review_id": ms2.get("docid"),
            "review_pmid": ms2.get("pmid"),
            "review_doi_present": bool(ms2.get("doi")),
            "report_pmids": sum(bool(ref.get("pmid")) for group in ms2.get("included_studies", []) for ref in group.get("references", [])),
            "report_dois": sum(bool(ref.get("doi")) for group in ms2.get("included_studies", []) for ref in group.get("references", [])),
            "trial_registration_identifiers": sum(bool(ref.get("identifiers")) for group in ms2.get("included_studies", []) for ref in group.get("references", [])),
            "effect_labels_are_gold": False,
            "effect_label_note": "sample includes significance probability/evidence fields, not a verified gold cross-study direction table",
        },
        "evidence_inference_2": {
            "annotation_rows": len(ann),
            "valid_annotation_rows": len(valid),
            "unique_prompt_ids": len({row["PromptID"] for row in prompts}),
            "unique_article_pmcids": len({row["PMCID"] for row in prompts}),
            "label_counts_valid": dict(Counter(row["Label"] for row in valid)),
            "prompt_rows_per_article_max": max(Counter(row["PMCID"] for row in prompts).values()),
            "article_ids_with_nct_or_trial_registration": sum(bool(re.search(r"NCT\\d+", (row.get("Outcome", "") + row.get("Intervention", "") + row.get("Comparator", "")), re.IGNORECASE)) for row in prompts),
            "pmcid_present": all(bool(row.get("PMCID")) for row in prompts),
            "doi_field_present": False,
            "trial_family_field_present": False,
            "split_counts": {name: len(values) for name, values in split_sets.items()},
            "split_intersections": split_intersections,
        },
        "prototype": {
            "clean_instances": sum(row["perturbation"]["type"] == "CLEAN" for row in proto),
            "omission_instances": sum(row["perturbation"]["type"] == "RANDOM_EVIDENCE_OMISSION" for row in proto),
            "unique_question_ids": len({row["question_id"] for row in proto}),
            "unique_article_ids": len({row["article_id"] for row in proto}),
            "trial_family_ids_available": sum(bool(row.get("trial_family_id")) for row in proto),
            "review_ids_available": sum(bool(row.get("review_id")) for row in proto),
            "supported_perturbations": ["RANDOM_EVIDENCE_OMISSION"],
            "unsupported_perturbations": ["DIRECTIONAL_CONTRADICTION", "PICO_NEAR_DISTRACTOR", "DUPLICATE_REPORT"],
        },
    }
    (repo / "data/manifests/milestone_1_audit.json").write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
