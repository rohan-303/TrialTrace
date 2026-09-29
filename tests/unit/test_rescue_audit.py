from __future__ import annotations

import json
from pathlib import Path


def test_milestone_1r_audit_has_verified_source_counts() -> None:
    path = Path("artifacts/milestone_1r/20260929_source_rescue/trialreviewbench_audit.json")
    if not path.exists():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    counts = data["counts"]
    assert counts["reviews_csv_rows"] == 100
    assert counts["search_screening_rows"] == 100
    assert counts["involved_citation_rows"] == 2220
    assert counts["extraction_files"] == 23
    assert counts["extraction_rows"] == 632
    assert counts["distinct_involved_pmids"] == 2132
    assert data["limitations"]
