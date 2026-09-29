# TrialTrace Project Specification

**Working title:** TrialTrace: Risk-Controlled Clinical Evidence Synthesis Under Missing, Conflicting, and PICO-Incompatible Evidence
**Milestone:** 1S — Review-Level Conclusion Stability Kill-Test
**Status:** `PROJECT_CLOSED_AFTER_FEASIBILITY_FAILURE`; no further model training, dataset acquisition, redesign, or experiments are authorized under this project.
**Specification date:** 2026-09-29 (US/Eastern)

## 1. Scientific question

When a clinical evidence set is incomplete, contradictory, duplicated, corrupted, or only superficially PICO-compatible, can an evidence-synthesis system determine whether the evidence justifies answering, should report conflict, or should abstain?

For question `q` and evidence set `E`, the primary decision object is:

`D(q,E) ∈ {SYNTHESIZE, CONFLICT, ABSTAIN}`

This is a benchmark question about selective evidence synthesis under evidence-set shift, not a claim of clinical decision support or autonomous medical advice.

## 2. Decision semantics

- **SYNTHESIZE:** evidence is sufficiently compatible and adequate for the benchmark’s frozen conclusion target; the system may report a direction/conclusion with provenance.
- **CONFLICT:** relevant, sufficiently compatible evidence contains material disagreement in direction or conclusion; the system must expose the disagreement rather than collapse it into a single confident direction.
- **ABSTAIN:** evidence is insufficient, PICO-incompatible, misleading, unavailable, duplicated without independent support, or otherwise below the frozen adequacy contract.

The benchmark must define these labels operationally per task family. They are not universal clinical truth labels.

## 3. Primary hypotheses

- **H1 — Evidence-set shift failure:** systems that perform acceptably on clean evidence collections exhibit increased unsupported or directionally incorrect synthesis under systematic omission, mismatch, duplication, truncation, and retrieval-failure perturbations.
- **H2 — Citation insufficiency:** citation correctness and evidence-span grounding do not by themselves guarantee whole-evidence-set adequacy.
- **H3 — Conflict collapse:** standard retrieval-plus-generation systems under-detect legitimate cross-study disagreement relative to a decision-aware adequacy evaluator.
- **H4 — Selective benefit:** an evidence-adequacy decision can reduce selective risk at matched coverage relative to answer-always baselines, but may lose coverage and may fail under unseen shifts.
- **H5 — Non-triviality gate:** any improvement must exceed simple, transparent heuristics such as evidence count, direction majority, span support, and duplicate suppression.

## 4. Rival explanations

The targeted failures may be artifacts of poor retrieval, label ambiguity, effect-size heterogeneity, context limits, or unrealistic synthetic perturbations. Standard calibration or proper scoring may already capture much of the benefit. A benchmark may also reward metadata shortcuts rather than clinical reasoning. Every claim must be tested against these alternatives.

## 5. Falsifiers and kill criteria

Stop or narrow the project if any of these holds:

1. **Novelty failure:** prior work already evaluates the same controlled medical evidence-set corruptions with explicit adequacy/conflict/abstention decisions and selective risk, leaving no non-trivial surviving contribution.
2. **Data failure:** review-to-study links, PICO/effect labels, trial-family identities, licensing, or document access cannot be verified well enough for a defensible benchmark.
3. **Label failure:** expert-independent perturbation labels cannot be defined deterministically or audited without an LLM being the sole oracle.
4. **Failure-mode failure:** strong baselines do not show meaningful degradation on realistic shifts, or degradation is explained entirely by retrieval recall and trivial heuristics.
5. **Method failure:** an adequacy method does not improve risk-coverage or conflict/unsupported-claim behavior beyond transparent baselines at matched resource budgets.
6. **Leakage failure:** trial families, reviews, registrations, or near-duplicates cross splits in a way that invalidates conclusions.
7. **Sufficiency failure:** available tasks do not support a clinically interpretable evidence-set decision and only support generic document classification.

A negative result is scientifically acceptable; silently changing the task to preserve the project is not.

## 6. Benchmark scope

Initial scope is retrospective, public, text-based, randomized-trial evidence synthesis. The first release should use one primary track with structured study-level evidence and one complementary multi-document track:

- **Study-level track:** Evidence Inference 2.0-style article + PICO prompt + effect direction + evidence span.
- **Review-set track:** MS²/MSLR-style systematic review with constituent studies and review-level structure.

PMC Open Access text may be used only after article-level license and source eligibility checks. Restricted or unclear reuse terms remain outside the benchmark until resolved.

## 7. Perturbation taxonomy

Each perturbation has a deterministic seed, parent-set identifier, transformation parameters, and a machine-readable rationale.

1. Random omission; progressive omission.
2. Strongest-positive, strongest-negative, and largest-study omission where effect/sample-size metadata exist.
3. Directional contradiction injection from compatible studies.
4. Population, intervention, comparator, and outcome mismatch.
5. Trial-family duplicate publication insertion.
6. Lexical/embedding near-match distractors.
7. Evidence sparsity.
8. Long-document/context truncation with location recorded.
9. Retrieval/tool failure: unavailable document, missing span, or failed retrieval response.
10. Combined shifts, reserved for stress tests after single-shift validity is established.

Synthetic perturbations must not be described as naturally occurring missingness. Natural and constructed shift regimes must be reported separately.

## 8. Provisional splits

Splits are provisional until schemas, identifiers, licenses, and duplicates are inspected. Primary split unit is the underlying trial/review family, never an individual passage or publication. No PMID, DOI, registration identifier, near-duplicate, or constituent report may cross train/calibration/test. Candidate policies: review-family holdout, trial-family holdout, specialty holdout, and temporal holdout where timestamps are available. Calibration is isolated from test and cannot use test outcomes.

## 9. Evaluation contract

Primary outcomes:

- selective risk–coverage curves and AURC;
- unsupported/directionally wrong synthesis rate conditional on answering;
- conflict detection precision/recall/F1;
- abstention quality and coverage;
- conclusion direction accuracy on answerable cases.

Secondary outcomes: retrieval Recall@k/MRR, PICO compatibility, evidence-span precision/recall/F1, citation precision/recall/entailment, omission sensitivity, calibration (ECE/Brier), robustness degradation by perturbation, tokens/tool calls/latency/cost, and GPU utilization when applicable. Use paired bootstrap confidence intervals after the unit of resampling is frozen.

Every system comparison must record model revision, corpus, retrieval budget, context budget, tool-call budget, decoding, prompt version, seed, and cost. Answer-always and transparent heuristic baselines are mandatory.

## 10. Non-claims

TrialTrace will not claim clinical safety, treatment efficacy, universal distribution-free guarantees, superiority over clinicians, or that conformal prediction remains guaranteed under intentional evidence-set shift. If conformal methods are later used, calibration distribution, exchangeability assumptions, and empirical degradation must be reported separately.

## 11. Milestone 1S closure

The Milestone 1S audit tested a strict hazard-ratio subset of TrialReviewBench. It found three review/outcome units and one non-preserving multi-report omission pair. Leave-one-report-out perturbations produced no transitions, while a five-report omission produced the only transition and was perfectly identified by a perturbation-size rule. The quantitative, counterfactual, and non-triviality gates therefore fail. The current TrialTrace direction is stopped; no method-development milestone is authorized.

## 12. Closeout boundary

The project is closed after Milestone 1S. Historical plans above remain part of the scientific record; they are not active work. Do not begin Milestone 2, method development, another dataset search, model benchmarking, or GPU execution within this repository. Any restart requires a new project proposal satisfying the conditions in `PROJECT_CLOSEOUT.md`.
