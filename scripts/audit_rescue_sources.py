from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "artifacts" / "milestone_1r" / "20260929_source_rescue"
TRB = BASE / "trialreviewbench"
OUT = BASE / "trialreviewbench_audit.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    reviews = list(csv.DictReader((TRB / "TrialReviewBench-reviews.csv").open(encoding="utf-8-sig", newline="")))
    search_rows = [json.loads(line) for line in (TRB / "TrialReviewBench-study-search-screening.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    extraction = []
    extraction_schemas = {}
    for path in sorted((TRB / "TrialReviewBench-data-extraction").glob("*.csv")):
        rows = list(csv.DictReader(path.open(encoding="utf-8-sig", newline="")))
        extraction.extend(rows)
        extraction_schemas[path.name] = {
            "rows": len(rows),
            "columns": list(rows[0]) if rows else [],
            "sha256": sha256(path),
            "pmid_values": sorted({r.get("PMID", "").strip() for r in rows if r.get("PMID", "").strip()}),
        }

    involved = []
    for row in search_rows:
        involved.extend(row.get("Involved_Citations", []))
    def vals(key: str):
        return [str(x.get(key, "")).strip() for x in involved if str(x.get(key, "")).strip()]

    review_pmids = {r.get("PMID", "").strip() for r in reviews if r.get("PMID", "").strip()}
    study_pmids = {x for x in vals("pmid") if x}
    nct_ids = {x for x in vals("nctid") if x}
    dois = {x.lower() for x in vals("doi") if x}
    extraction_pmids = {r.get("PMID", "").strip() for r in extraction if r.get("PMID", "").strip()}
    extraction_columns = sorted({c for r in extraction for c in r})
    topic_counts = Counter(r.get("Topic", "") for r in reviews)
    review_sizes = [len(r.get("Involved_Citations", [])) for r in search_rows]
    result = {
        "source": "zifeng-ai/TrialReviewBench",
        "retrieval": {
            "repository": "https://huggingface.co/datasets/zifeng-ai/TrialReviewBench",
            "revision": "main at retrieval time; commit not pinned by URL",
            "license": "apache-2.0 dataset card",
            "files": {p.name: {"bytes": p.stat().st_size, "sha256": sha256(p)} for p in [TRB / "README.md", TRB / "TrialReviewBench-reviews.csv", TRB / "TrialReviewBench-study-search-screening.jsonl"]},
        },
        "counts": {
            "reviews_csv_rows": len(reviews),
            "search_screening_rows": len(search_rows),
            "distinct_review_pmids": len(review_pmids),
            "involved_citation_rows": len(involved),
            "distinct_involved_pmids": len(study_pmids),
            "distinct_nct_ids": len(nct_ids),
            "distinct_dois": len(dois),
            "extraction_rows": len(extraction),
            "extraction_files": len(extraction_schemas),
            "extraction_distinct_pmids": len(extraction_pmids),
            "review_involved_count_min": min(review_sizes),
            "review_involved_count_max": max(review_sizes),
            "review_involved_count_mean": sum(review_sizes) / len(review_sizes),
        },
        "coverage": {
            "involved_pmid_fraction": len(study_pmids) / len(involved),
            "involved_doi_fraction": len(dois) / len(involved),
            "involved_nct_fraction": len(nct_ids) / len(involved),
            "extraction_pmid_fraction": len(extraction_pmids) / len(extraction),
            "review_pmids_in_involved": len(review_pmids & study_pmids),
            "extraction_pmids_in_involved": len(extraction_pmids & study_pmids),
        },
        "topics": dict(topic_counts),
        "schema": {
            "search_screening_keys": sorted(search_rows[0]),
            "involved_citation_keys": sorted(involved[0]),
            "extraction_union_columns": extraction_columns,
            "extraction_per_file": extraction_schemas,
        },
        "limitations": [
            "The extraction CSV files have heterogeneous, review-specific columns; the HF dataset viewer reports a schema cast failure.",
            "The release provides report-level PMID/DOI/NCT fields where present but no explicit trial-family identifier.",
            "The release contains review-to-included-report relationships and manually checked extraction rows, but not a verified independent cross-review trial-family graph.",
            "The repository URL is mutable main rather than a pinned immutable revision unless the recorded commit is added separately.",
        ],
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["counts"], indent=2, sort_keys=True))
    print(json.dumps(result["coverage"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
