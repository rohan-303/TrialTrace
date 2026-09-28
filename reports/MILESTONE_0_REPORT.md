# Milestone 0 report

## MILESTONE

**Milestone 0 — Research Specification and Novelty Kill-Test**
**Status: CONDITIONAL** — foundation and targeted kill-test completed; no empirical benchmark or model experiment executed.

## WHAT WAS COMPLETED

- Created a fresh local Git repository at `C:/Users/rohan/TrialTrace`.
- Wrote canonical `PROJECT_SPEC.md` with formal decision semantics, hypotheses, falsifiers, perturbation taxonomy, split contract, evaluation protocol, non-claims, and continuation rule.
- Added restrained research repository structure, `pyproject.toml`, package smoke test, `.gitignore`, and `AGENTS.md`.
- Completed a targeted primary-source audit of MS², Evidence Inference 2.0, OpenScholar, PaperQA2/LitQA2, TrialMind/TrialReviewBench, and MedSR-Copilot/MedSR-Bench repository materials.
- Documented unresolved LEADS identity rather than inventing a comparison.
- Wrote data/schema/license feasibility and roadmap/gate documents.

## SCIENTIFIC FINDINGS

The project’s strongest defensible contribution is currently a **benchmark/evaluation protocol**, not a new synthesis agent: controlled medical evidence-set corruption with explicit `SYNTHESIZE / CONFLICT / ABSTAIN` semantics and selective risk–coverage analysis. OpenScholar and PaperQA2 are strong answer-quality/provenance/contradiction threats; TrialMind and MedSR-Copilot are direct medical workflow/benchmark threats. The available audit does not establish that any prior work already performs the exact combination, but it also does not justify a novelty claim yet.

MS² offers review–constituent-study structure but has licensing and trial-family identity risks. Evidence Inference 2.0 offers RCT article, prompt, direction, and evidence-span structure but is primarily study-level and does not by itself provide cross-study compatibility or answerability labels. Combining them is feasible only after source-version, license, identifier, and leakage audits.

## KEY METRICS

No scientific metrics were computed. This milestone intentionally produced **zero benchmark results, zero model results, and zero claims of baseline failure**.

## GATES

- **Specification gate — PASS:** formal question, labels, hypotheses, falsifiers, perturbations, splits, metrics, and non-claims are documented.
- **Novelty gate — CONDITIONAL:** plausible evaluation gap survives, but MedSR-Bench overlap, LEADS identity, and broader selective-RAG/provenance coverage remain unresolved.
- **Data gate — CONDITIONAL:** candidate sources and likely uses are verified at README/abstract level, but legal/version/schema/trial-family checks are not complete.
- **Failure-mode gate — NOT COMPUTED:** no baselines have run.
- **Method gate — NOT COMPUTED:** no method exists or has been evaluated.
- **Reproducibility foundation gate — PASS:** fresh repository, immutable-output rules, source-layout package, smoke test, and data-boundary rules exist.
- **Overall continuation gate — CONDITIONAL:** recommend Milestone 1 only as a bounded data/overlap audit, after external review; do not begin method development.

## ARTIFACTS

- `PROJECT_SPEC.md`
- `README.md`
- `AGENTS.md`
- `docs/NOVELTY_AUDIT.md`
- `docs/DATA_FEASIBILITY.md`
- `docs/ROADMAP_AND_GATES.md`
- `pyproject.toml`
- `src/trialtrace/__init__.py`
- `tests/unit/test_foundation.py`

## GIT

- Branch: `main`
- Commit: `6df6eb4062c85ebd7bdfa4b2eff9da52dc24a965` (`docs: establish TrialTrace milestone 0 foundation`).
- Remote/push: no remote configured; no push performed.
- Worktree: clean after commit.

## RISKS / PROBLEMS

1. MedSR-Bench’s primary paper and dataset card must be inspected before claiming a surviving benchmark gap.
2. The exact LEADS work was not uniquely identified; it is intentionally excluded from substantive claims.
3. Trial-family identity, source licenses, and deterministic three-way labels are not yet verified.

## RECOMMENDED NEXT MILESTONE

After external review, run **Milestone 1 — Data and Benchmark Construction**, beginning with the MedSR-Bench overlap audit and authoritative MS²/Evidence Inference version/license/schema inspection. Freeze no benchmark until trial-family leakage and label integrity pass.

## Sources

- https://github.com/allenai/ms2
- https://raw.githubusercontent.com/allenai/ms2/master/README.md
- https://arxiv.org/abs/2104.06486
- https://github.com/jayded/evidence-inference
- https://raw.githubusercontent.com/jayded/evidence-inference/master/README.md
- https://arxiv.org/abs/2005.04177
- https://arxiv.org/abs/2411.14199
- https://arxiv.org/abs/2409.13740
- https://arxiv.org/abs/2406.17755
- https://github.com/MAGIC-AI4Med/MedSR-Copilot
- https://huggingface.co/datasets/halfmorepiece/MedSR-Bench
