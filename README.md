# TrialTrace

TrialTrace studies whether clinical evidence-synthesis systems know when an evidence set does **not** justify a conclusion.

## Current status

**Milestone 1S — TRIALTRACE_STOP.** The final conclusion-stability kill-test found only three strict quantitative review/outcome units, one non-preserving counterfactual, and a perturbation-size shortcut that perfectly identified the only transition. No TrialTrace model, training, or expensive experiment was run.

## Core decision

The final tested formulation was paired review-level conclusion stability under controlled evidence-set shifts. It was stopped because the available TrialReviewBench release could not support a non-trivial benchmark.

## Repository rules

- Do not download or process restricted medical data.
- Do not overwrite frozen artifacts or scientific result directories.
- Every future run gets a unique output directory and manifest.
- Every claim must distinguish verified, executed, reproduced, validated, and not computed.
- This is a research benchmark, not a clinical decision-support product.

## Planned commands

Implementation commands will be added only after Milestone 0 review and the data contract gate.
