# Canonical TrialTrace prototype schema v0.1

## Status

This is an executed **study-level feasibility schema**, not a frozen multi-study benchmark schema. It intentionally preserves unavailable relationships as `null`.

## One JSONL object

- `instance_id`: SHA-256 of the canonical instance payload excluding the ID.
- `question_id`: Evidence Inference prompt identity.
- `question`: rendered intervention/comparator/outcome question.
- `review_id`: review identifier; `null` in the EI-only prototype.
- `trial_family_id`: underlying-trial identity; `null` because the source has no trial-family field.
- `report_id`: source report identifier, currently `pmcid:<id>`.
- `article_id`: PMCID-qualified article identity.
- `pico`: object with `population`, `intervention`, `comparator`.
- `outcome_identity`: source prompt outcome string; no normalization is applied.
- `effect_direction`: `INCREASED`, `DECREASED`, or `NO_DIFFERENCE`, derived from valid EI annotations by deterministic majority with lexical tie-break.
- `evidence_spans`: annotation-derived evidence offsets and text.
- `provenance`: source name, PMCID, PromptID, annotation count, and label rule.
- `evidence_set`: report IDs visible to the instance.
- `perturbation`: type, seed, parent, removed reports, and semantic rationale.
- `expected_decision`: `SYNTHESIZE` for a valid clean one-report instance; `ABSTAIN` after sole-report omission.

## Explicit limitations

The prototype cannot represent a defensible `CONFLICT` label because it does not contain multiple independently identified compatible trial families for one PICO question. It cannot represent duplicate-report perturbations because no trial-family identifiers are present. It cannot create a valid PICO distractor without an externally audited compatibility relation. These are recorded as unsupported, not guessed.
