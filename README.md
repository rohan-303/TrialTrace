# TrialTrace

TrialTrace studies whether clinical evidence-synthesis systems know when an evidence set does **not** justify a conclusion.

## Current status

**Milestone 1 — REDESIGN_REQUIRED.** The data feasibility prototype executed successfully, but the current sources do not support the full multi-study TrialTrace benchmark. No model, training, or expensive experiment has been run.

## Core decision

For a question `q` and evidence set `E`, evaluate `SYNTHESIZE`, `CONFLICT`, or `ABSTAIN` under controlled evidence-set shifts.

## Repository rules

- Do not download or process restricted medical data.
- Do not overwrite frozen artifacts or scientific result directories.
- Every future run gets a unique output directory and manifest.
- Every claim must distinguish verified, executed, reproduced, validated, and not computed.
- This is a research benchmark, not a clinical decision-support product.

## Planned commands

Implementation commands will be added only after Milestone 0 review and the data contract gate.
