# TrialTrace Scientific Closeout

**Canonical status:** `PROJECT_CLOSED_AFTER_FEASIBILITY_FAILURE`
**Final milestone:** Milestone 1S — Review-Level Conclusion Stability Kill-Test
**Master decision:** `TRIALTRACE_STOP`
**Closeout date:** 2026-09-29 (US/Eastern)

## Original scientific goal

TrialTrace asked whether clinical evidence-synthesis systems could perform risk-controlled multi-trial synthesis when evidence was missing, contradictory, duplicated, corrupted, or PICO-incompatible, including recognizing when a conclusion should be revised or withheld.

The intended contribution was a controlled, provenance-preserving evaluation of evidence-set changes rather than another general systematic-review agent.

## Major project stages

- **Milestone 0 — Research specification and novelty kill-test:** formalized the scientific question, perturbations, gates, leakage controls, and initial novelty threats.
- **Milestone 1 — Data and benchmark feasibility:** audited MS² and Evidence Inference 2.0 and demonstrated that the initial prototype lacked trial-family identity, multi-study labels, and non-trivial task semantics.
- **Milestone 1R — Multi-study rescue:** audited TrialReviewBench and investigated Epistemonikos/ED-Trials. TrialReviewBench supplied report-level review structure, but auditable trial-family linkage and a common outcome ontology were not established.
- **Milestone 1S — Conclusion-stability kill-test:** audited structured quantitative extraction, recomputed a strict hazard-ratio subset, and tested paired evidence-set perturbations. The resulting candidate was too small and was solved by perturbation severity.

## Final decision and reasons for stopping

The current publicly auditable data path does not support a publishable implementation under the project specification. The project did **not** establish that the underlying scientific idea is universally impossible; it established that this implementation path failed its feasibility and non-triviality gates.

Major empirical reasons:

1. Reliable underlying trial-family identity was not available.
2. Defensible multi-study `SYNTHESIZE / CONFLICT / ABSTAIN` labels were not available.
3. TrialReviewBench extraction schemas were substantially heterogeneous.
4. Only **3** strict quantitative review/outcome units were recoverable.
5. Only **28** HR records were parseable for deterministic pooling.
6. Leave-one-report-out perturbations produced **0** conclusion transitions.
7. Only **1** non-preserving transition was observed, requiring removal of five reports.
8. The paired candidate set was severely imbalanced: 28 preserve versus 1 transition.
9. An omission-size rule achieved **1.000** accuracy on the candidate transition set.
10. Novelty overlap increased with the 2026 Evidence Sufficiency Benchmark, MetaSyn, TrialMind/TrialReviewBench, MedSR-Bench, and auditable evidence-compilation work.

## Reusable scientific lessons

- Test trial-family identity before model development.
- Do not equate publication-level identity with independent-trial identity.
- Require benchmark labels to survive trivial metadata baselines.
- Build matched counterfactual controls before interpreting perturbation results.
- Treat perturbation severity as a potential label leak.
- Freeze estimands, outcome mappings, and analysis membership before statistical recomputation.
- Expect heterogeneous systematic-review extraction schemas to constrain automated benchmark construction.
- Re-run the novelty audit after every major project redesign.
- Preserve negative results as scientific evidence rather than weakening the target until it becomes feasible.

## Reusable assets

| Asset | Location | General reuse | TrialTrace-specific status |
|---|---|---|---|
| Source-manifest and SHA-256 conventions | `docs/DATA_MANIFEST.md`, `scripts/audit_sources.py`, `scripts/audit_rescue_sources.py` | Yes: provenance and immutable-source audits | Source names and milestone paths are project-specific |
| Deterministic artifact boundaries | `AGENTS.md`, `.gitignore`, milestone reports | Yes: keep raw/restricted data and results outside Git | Directory rules are TrialTrace-specific |
| Benchmark schema and leakage checks | `docs/BENCHMARK_SCHEMA.md`, `docs/LEAKAGE_AUDIT.md` | Yes: audit identities, splits, and provenance before benchmarking | Trial-family fields and source contracts are TrialTrace-specific |
| Perturbation provenance conventions | `docs/PERTURBATION_SPEC.md` | Yes: parent IDs, seeds, transformation parameters, and rationale | Original perturbation taxonomy is TrialTrace-specific |
| Metadata leakage tests | `docs/HEURISTIC_SANITY.md`, `scripts/build_prototype.py` | Yes: require transparent baselines before claiming benchmark difficulty | Historical prototype labels are not reusable benchmark data |
| Conclusion-stability audit | `scripts/audit_conclusion_stability.py`, `tests/unit/test_conclusion_stability_audit.py` | Yes: deterministic effect recomputation and omission audit pattern | TrialReviewBench paths and selected HR schemas are TrialTrace-specific |
| Staged scientific gates | `docs/ROADMAP_AND_GATES.md`, milestone reports | Yes: explicit PASS/CONDITIONAL/FAIL continuation decisions | Gate thresholds and project decisions are TrialTrace-specific |

Failed prototype labels, TrialReviewBench source files, and ignored raw records are **not** released reusable benchmark data.

## Preservation boundary

Historical milestone reports remain unchanged. No additional research experiments, model runs, dataset searches, or redesigns are authorized by this closeout. Any future work using the assets must be proposed as a new project with a new scope and provenance contract.
