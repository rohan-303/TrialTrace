# TrialTrace agent rules

## Scope

TrialTrace is in Milestone 0. Do not implement models, acquire large datasets, run experiments, or change the scientific question without an approved milestone transition.

## Research integrity

- Preserve failed hypotheses and invalidated runs; never delete them to improve a narrative.
- Use source-backed claims and record access/license uncertainty explicitly.
- Never use an LLM as the sole benchmark-label oracle.
- Keep trial-family and review-family leakage controls explicit.
- Do not claim clinical validity or distribution-free guarantees under evidence-set shift.

## Engineering

- Python 3.11+ target; current host interpreter is Python 3.14.7.
- Use typed, modular, configuration-driven code.
- Run tests and inspect the complete staged diff before milestone commits.
- Never commit secrets, credentials, raw restricted data, model caches, or generated results.
