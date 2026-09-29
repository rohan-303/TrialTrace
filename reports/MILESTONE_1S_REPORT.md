# Milestone 1S — Review-Level Conclusion Stability Kill-Test

**Date:** 2026-09-29
**Master decision:** `TRIALTRACE_STOP`

## Scope

This milestone tested whether TrialReviewBench can support a non-trivial, objectively labeled benchmark of review-level conclusion stability under controlled evidence-set perturbations. It did not run LLMs, train models, use GPUs, or create a TrialTrace model.

## Master decision

**`TRIALTRACE_STOP`** for the current TrialTrace direction.

A narrow deterministic calculation is possible, but the available release does not support a defensible benchmark of useful scale or diversity. The strict quantitative subset contains only three review/outcome units. Leave-one-report-out perturbations never changed the conclusion class. The first transition required removing five of ten reports from one PFS review, and a report-count threshold identified that transition perfectly in the tiny constructed set. The resulting phenomenon is therefore not yet a non-trivial benchmark rather than a viable basis for method development.

This is a stop of the current TrialTrace research direction, not a claim that evidence-set conclusion stability is scientifically unimportant.

## Data subset

TrialReviewBench was not re-downloaded. The frozen Milestone 1R source files were audited in place.

| Quantity | Verified count |
|---|---:|
| Reviews | 100 |
| Extraction schemas/files | 23 |
| Extraction rows | 632 |
| Files with explicit HR + 95% CI columns | 2 |
| Files with explicit OR/RR + 95% CI columns | 0 |
| Files with event-like fields | 4 |
| Files with explicit mean ± SD fields | 1 |
| Strict quantitative review/outcome units | 3 |
| Parseable HR records in strict subset | 28 |

The 23 schemas are review-specific and heterogeneous. Most rows contain descriptive study characteristics rather than arm-level quantitative outcome data suitable for deterministic recomputation. Event-like fields are not sufficient by themselves: they are not consistently paired with intervention/comparator, outcome, and arm-level denominators.

Strict units:

| Review PMID | Outcome | Records | Effect | Clean pooled HR (95% CI) | Clean class |
|---|---|---:|---|---|---|
| 32899139 | PFS | 8 | HR | 0.548 (0.504, 0.594) | FAVORABLE |
| 35093742 | OS | 10 | HR | 0.703 (0.654, 0.755) | FAVORABLE |
| 35093742 | PFS | 10 | HR | 0.741 (0.637, 0.863) | FAVORABLE |

The calculations used inverse-variance pooling of log-HR estimates and reported confidence intervals. A DerSimonian–Laird random-effects variance was used; when estimated heterogeneity was zero, this equals the fixed-effect result.

## Clean reproduction

Clean-set recomputation was source-checked against the TrialReviewBench review abstracts, not treated as a replacement for a full published forest-plot audit.

- **32899139:** recomputed PFS direction was favorable and consistent with the abstract’s statement that CDK4/6 inhibitor addition improved PFS. The abstract did not provide a comparable pooled numeric PFS estimate in the inspected text.
- **35093742 OS:** recomputed HR **0.703 (0.654–0.755)** versus published abstract HR **0.71 (0.66–0.76)**. Direction and approximate magnitude agree.
- **35093742 PFS:** recomputed HR **0.741 (0.637–0.863)** versus published abstract HR **0.78 (0.66–0.93)**. Direction agrees; numerical differences are plausible given the extracted records and pooling choices but were not independently reconciled to the publication’s exact analysis membership.

**Clean-Reproduction Gate: CONDITIONAL**, not PASS. Two units have directionally consistent results and one has close numeric agreement, but the subset is too small and the exact source-analysis membership/estimand reconciliation is incomplete.

## Conclusion contract

The provisional deterministic contract was:

- `FAVORABLE`: pooled HR confidence interval entirely below 1.
- `UNFAVORABLE`: pooled HR confidence interval entirely above 1.
- `UNCERTAIN`: pooled HR confidence interval crosses 1.
- Transition label `PRESERVE`: perturbed class equals clean class.
- Transition label `REVISE`: perturbed class differs from clean class.

`WITHHOLD` was not frozen. The available data did not establish a defensible evidence-sufficiency threshold independent of arbitrary report count or meta-analytic convention.

## Perturbations

- Leave-one-report-out: **28** paired perturbations across the three units.
- Leave-one-report-out transitions: **0**.
- Exhaustive multi-report omission search on 35093742/PFS: no transition through removal of four reports.
- First transition: remove five source rows, producing pooled HR **0.918 (0.830–1.016)** and changing `FAVORABLE` to `UNCERTAIN`.
- 35093742/OS: no non-FAVORABLE class through exhaustive removal of one to six of ten reports.

No synthetic clinical results, cross-review substitutions, PICO distractors, or trial-family claims were created.

## Counterfactual pairs

- Clean review/outcome units: **3**.
- Leave-one-out pairs: **28**, all `PRESERVE`.
- Non-preserving multi-report pairs: **1**, `FAVORABLE → UNCERTAIN`.
- `PRESERVE → REVISE`: **1** under the provisional transition encoding, but only after a five-report omission in one review/outcome unit.
- `PRESERVE → WITHHOLD`: **0**.

The pair set is not balanced, not review-independent, and not large enough for a benchmark split.

## Human/source verification

No qualified biomedical expert annotation was performed. The subset is classified as **SOURCE_VERIFIED**, not expert-verified.

Verified from the frozen TrialReviewBench source files:

- review PMID, title, abstract, and PICO fields;
- extraction headers and source rows;
- reported HR/CI strings used in the strict subset;
- deterministic recomputation and source hashes.

The published abstract was used for reference comparison. No LLM-generated summary or label was used.

## Triviality baselines

For the 29 tiny paired instances consisting of 28 leave-one-out cases plus one first transition:

- Always predict `PRESERVE`: **28/29 = 0.9655** accuracy.
- Predict a transition when five or more reports are removed: **29/29 = 1.0000** accuracy.

The second rule is a direct perturbation-size shortcut, not meaningful evidence reasoning. The candidate benchmark therefore fails the non-triviality requirement.

No logistic-regression or tree model was trained because the candidate set was already demonstrably degenerate and would make such estimates misleading.

## Novelty result

The novelty audit was updated to include the following closest work:

- **Evidence Sufficiency Benchmark**, DOI `10.32604/cmc.2026.086343`: directly covers full, partial, irrelevant, absent, and conflicting evidence with answer/abstain calibration and evidence-sufficiency curves. Generic sufficiency and abstention are not TrialTrace novelty.
- **MetaSyn**, arXiv `2606.17041`: provides expert-curated meta-analyses, PI/ECO criteria, included studies, hard negatives, PubMed linkage, and stage-wise retrieval/screening/synthesis evaluation. PICO-aware retrieval or hard-negative screening is not sufficient novelty.
- **Auditable evidence compiler**, DOI `10.64898/2026.09.21.26363538`: connects evidence identities, populations, outcomes, statistical roles, dependence/overlapping participants, corrections, supersession, deterministic statistics, refusal states, and auditable releases. Provenance alone is not sufficient novelty.
- **TrialMind / TrialReviewBench:** already covers clinical review workflow, extraction, and synthesis evaluation.
- **MedSR-Copilot / MedSR-Bench:** remains a direct medical systematic-review workflow overlap; public benchmark semantics were not sufficient to rescue this milestone.
- Recent numerical extraction and meta-analysis automation work, including the 2025 meta-analysis extraction benchmark, further reduces the novelty of treating structured extraction alone as the contribution.

The proposed counterfactual conclusion-stability formulation remains conceptually distinct from these works, but this data audit did not establish a usable, non-trivial implementation. No positive novelty claim is made.

## Gates

| Gate | Status | Justification |
|---|---|---|
| Quantitative Data | **FAIL** | Only two schemas contain explicit HR+CI columns; no common binary/continuous effect family was recoverable at useful scale. |
| Clean Reproduction | **CONDITIONAL** | Directional agreement in three units; one close numeric match; exact analysis membership not fully reconciled. |
| Conclusion Stability | **CONDITIONAL** | One objective transition exists, but only after a severe five-report omission in one unit. |
| Counterfactual | **FAIL** | Only one non-preserving pair; no WITHHOLD class; no balanced or independent pairs. |
| Non-Triviality | **FAIL** | Perturbation size perfectly predicts the only transition in the candidate set. |
| Ground Truth | **CONDITIONAL** | Statistical labels are deterministic and source-linked, but the reference subset is not expert-adjudicated. |
| Novelty | **CONDITIONAL** | The exact counterfactual object may remain distinct; useful benchmark viability was not established. |
| Release | **CONDITIONAL** | Hashes and deterministic audit are feasible; source text and rights remain external/source-specific. |
| Reproducibility | **PASS** | Audit script, frozen source paths, deterministic calculations, and output hash are recorded. |

## Artifacts

- `scripts/audit_conclusion_stability.py`
- `artifacts/milestone_1s/20260929_conclusion_stability_audit_01/conclusion_stability_audit.json`
- `reports/MILESTONE_1S_REPORT.md`
- Updated `docs/NOVELTY_AUDIT.md`
- Updated `docs/DATA_FEASIBILITY.md`
- Updated `PROJECT_SPEC.md`
- Updated `README.md`

The TrialReviewBench source files remain ignored and outside Git. No restricted source text, model output, credentials, or generated clinical labels were committed.

## Tests / integrity

- Deterministic audit executed successfully.
- Python compilation passed.
- Schema inventory counts and pooled estimates were emitted to JSON.
- SHA-256 hashes were recorded for all 23 extraction CSVs.
- No GPU, LLM, training, fine-tuning, or expensive experiment was run.

## GIT

- Branch: `main`
- Commit: `1b5c946` (`feat: test review-level conclusion stability`)
- Remote: `https://github.com/rohan-303/TrialTrace.git`
- Push: verified to `origin/main`
- Tag: none
- Worktree: clean after commit

## Risks

1. This stop decision is source- and release-specific; a legally auditable dataset with complete forest-plot data could support a different future project, but that would require a new scientific proposal.
2. The extracted HR records may represent subgroup/analysis selections that are not fully reconstructible from the public extraction tables alone.
3. The apparent transition requires a large, direction-targeted omission and may not represent a realistic evidence-set failure distribution.

## Recommended next milestone

No TrialTrace Milestone 2 or method-development milestone is recommended. The current TrialTrace direction should stop at Milestone 1S. Any restart should be treated as a new project proposal with a new primary source, frozen estimand, expert-verified analysis membership, and a pre-registered non-triviality test.
