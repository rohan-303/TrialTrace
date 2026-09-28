import json
from pathlib import Path

from trialtrace.prototype import random_omission, stable_id


def test_stable_id_is_order_independent() -> None:
    assert stable_id({"b": 2, "a": 1}) == stable_id({"a": 1, "b": 2})


def test_omission_is_deterministic() -> None:
    instance = {
        "instance_id": "parent",
        "report_id": "pmcid:1",
        "evidence_set": ["pmcid:1"],
        "evidence_spans": [{"evidence_id": "span"}],
        "expected_decision": "SYNTHESIZE",
    }
    first = random_omission(instance, 17)
    second = random_omission(instance, 17)
    assert first == second
    assert first["evidence_set"] == []
    assert first["expected_decision"] == "ABSTAIN"


def test_prototype_lines_are_json(tmp_path: Path) -> None:
    path = tmp_path / "prototype.jsonl"
    path.write_text(json.dumps({"instance_id": "x"}) + "\n", encoding="utf-8")
    assert json.loads(path.read_text(encoding="utf-8"))["instance_id"] == "x"
