import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).parents[2] / "scripts" / "audit_conclusion_stability.py"
SPEC = importlib.util.spec_from_file_location("audit_conclusion_stability", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
decision = MODULE.decision
meta_analysis = MODULE.meta_analysis
read_schema_inventory = MODULE.read_schema_inventory


def test_meta_analysis_and_decision() -> None:
    summary = meta_analysis([(0.6, 0.5, 0.72), (0.7, 0.58, 0.84)])
    assert summary["k"] == 2
    assert summary["pooled_hr"] < 1
    assert decision(summary) == "FAVORABLE"


def test_inventory_has_frozen_trialreviewbench_shape() -> None:
    source = Path("artifacts/milestone_1r/20260929_source_rescue/trialreviewbench/TrialReviewBench-data-extraction")
    inventory = read_schema_inventory(source)
    assert inventory["files"] == 23
    assert inventory["rows"] == 632
    assert inventory["hr_ci_files"] == 2
    assert inventory["or_rr_ci_files"] == 0
