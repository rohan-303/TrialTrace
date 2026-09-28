# Perturbation specification v0.1

## Deterministic supported perturbation

### `RANDOM_EVIDENCE_OMISSION`

Input: one valid Evidence Inference prompt with one report.
Rule: remove the sole report using a supplied integer seed and record the parent instance.
Output: empty evidence set, empty evidence spans, and expected `ABSTAIN` under the prototype’s explicit insufficiency contract.

The current implementation uses `seed + row_index` for each generated omission, records the removed report ID, and computes a new canonical SHA-256 instance ID. Re-running with the same source rows, limit, and seed produced the same output hash during this milestone.

## Unsupported perturbations

- `DIRECTIONAL_CONTRADICTION`: requires compatible multi-study effect directions; unavailable in the prototype.
- `PICO_NEAR_DISTRACTOR`: requires an audited compatibility relation across articles; unavailable.
- `DUPLICATE_REPORT`: requires underlying trial-family linkage; unavailable.
- asymmetric strongest-positive/negative omission: requires cross-study gold direction and study-level effect magnitude/sample size; unavailable.

The prototype’s omission task is a feasibility probe only. It should not be presented as the proposed TrialTrace benchmark because an evidence-count rule solves it directly.
