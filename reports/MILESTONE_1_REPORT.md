# Milestone 1 report

## MILESTONE

**Milestone 1 — Novelty Closure, Data Feasibility, and Benchmark Prototype**

## MASTER DECISION

# REDESIGN_REQUIRED

The benchmark direction remains potentially publishable, but the inspected public data cannot support the original multi-study `SYNTHESIZE / CONFLICT / ABSTAIN` benchmark without an additional audited source or human-verified subset.

## WHAT WAS COMPLETED

- Verified the local repository, expected Milestone 0 commit, clean state, empty GitHub repository, and repository identity.
- Configured `origin` as `https://github.com/rohan-303/TrialTrace.git`.
- Pushed the existing Milestone 0 commit without rewriting history.
- Audited actual MS² sample and MSLR2022 source documentation.
- Downloaded and hashed the official Evidence Inference 2.0 archive.
- Extracted and inspected actual EI v2.0 CSVs and split files.
- Implemented a bounded, deterministic EI study-level prototype.
- Implemented deterministic single-report omission.
- Added schema, perturbation, manifest, leakage, and heuristic documentation.
- Added tests and artifact/audit scripts.
- Did not train models, call large language models, use the dual-4090 server, or run expensive experiments.

## NOVELTY RESULT

The bounded primary-source audit did not identify an exact prior benchmark combining deterministic clinical evidence-set corruption, explicit `SYNTHESIZE / CONFLICT / ABSTAIN` semantics, trial-family leakage control, and selective risk–coverage evaluation.

This remains an unresolved gap rather than a confirmed novelty claim.

Already established by inspected work:

- systematic-review workflow automation: TrialMind and MedSR-Copilot;
- citation-backed scientific synthesis: OpenScholar and PaperQA2;
- contradiction discovery: PaperQA2;
- study-level ICO/effect direction and evidence spans: Evidence Inference 2.0;
- abstention, calibration, and risk–coverage methodology: broader selective prediction/RAG literature.

The public MedSR-Bench page is currently empty and the MedSR-Copilot repository marks its paper as coming soon. This reduces the immediate overlap threat but does not close it.

The exact intended LEADS work could not be identified from bounded primary-source searches. No substantive claims about LEADS were made.

## DATA RESULT

### MS² / MSLR2022

From the official MS² sample and MSLR2022 documentation:

- sample review count: 1;
- included study groups/reports in sample: 20;
- report PMIDs: 20/20;
- report DOIs: 0/20;
- trial-registration identifiers: 0;
- sample effect fields are not treated as verified gold cross-study direction labels;
- MSLR2022 README describes approximately 20K reviews and 470K studies and a 253 MB direct archive;
- licensing is not reducible to the repository’s Apache-2.0 code license; the README references the Semantic Scholar API and Dataset License Agreement.

The sample is suitable for schema inspection but not sufficient to establish trial-family or conflict-label feasibility.

### Evidence Inference 2.0

Measured from the official `v2.0.tar.gz` archive:

- annotation rows: **24,686**;
- valid-label rows: **24,321**;
- unique prompts: **12,865**;
- unique PMCIDs: **3,372**;
- train articles: **3,562**;
- validation articles: **443**;
- test articles: **449**;
- train/validation/test article-ID intersections: **0 / 0 / 0**;
- maximum prompts per article: **72**;
- PMCID available: yes;
- DOI field: absent;
- trial-family field: absent;
- trial-registration field: absent.

The valid-label data contains **619** rows with label `significantly increase`, while the official download documentation specifies `significantly increased`. These rows were excluded rather than silently normalized.

The repository code is MIT-licensed. That does not by itself establish unrestricted redistribution rights for all underlying article text.

## PROTOTYPE

Generated artifact:

`data/processed/prototype/trialtrace_prototype_v0_1.jsonl`

Counts:

- clean instances: **64**;
- omission instances: **64**;
- total instances: **128**;
- unique question IDs: **64**;
- unique article IDs: **6**;
- trial-family IDs: **0**;
- review IDs: **0**.

Supported perturbation:

- `RANDOM_EVIDENCE_OMISSION`: 64 instances.

Unsupported and explicitly not generated:

- directional contradiction;
- asymmetric strongest-positive/negative omission;
- PICO-near distractor;
- duplicate-report perturbation;
- trial-family-aware perturbations.

The prototype schema is documented in `docs/BENCHMARK_SCHEMA.md`.

## TRIAL-FAMILY ANALYSIS

No exact registration identifiers, DOI fields, or trial-family fields were available in the inspected EI v2.0 schema. PMCID identifies an article/report, not necessarily an underlying trial.

The feasible identity hierarchy is therefore:

1. exact registration match — unavailable;
2. explicit dataset trial-family linkage — unavailable;
3. article-level PMCID identity — available;
4. heuristic metadata linkage — not attempted to avoid manufacturing trial families;
5. unresolved — default for underlying trial identity.

Article-level split leakage can be controlled using the provided EI split files. Trial-family leakage cannot currently be controlled from these fields alone.

## LABEL SEMANTICS

The prototype can objectively derive:

- study-level effect direction from valid EI labels using deterministic majority with lexical tie-break;
- `SYNTHESIZE` for a valid clean one-report instance under the prototype contract;
- `ABSTAIN` after removing the sole report.

The prototype cannot objectively support:

- legitimate multi-study `CONFLICT`;
- duplicate-report independence errors;
- PICO-incompatible distractor semantics;
- evidence-set completeness beyond the presence/absence of one report.

The omission label is therefore a feasibility label, not a valid representation of the full TrialTrace scientific target.

## HEURISTIC SANITY CHECK

A rule that predicts `SYNTHESIZE` when `evidence_set` is non-empty and `ABSTAIN` otherwise achieved:

- **1.000 accuracy over 128 prototype rows.**

This is a serious triviality warning. It occurs because the current prototype exposes its answerability label through evidence count. The result is not a method result and does not support benchmark readiness.

## LEAKAGE AUDIT

- EI official article splits are pairwise disjoint in the inspected split files.
- Multiple prompts per article are present and must remain grouped by PMCID.
- No trial-family leakage audit can be completed from current fields.
- The bounded prototype does not freeze train/calibration/test splits.
- Exact duplicate/title/trial-family merging was not performed because the available identifiers do not justify it.

## KEY METRICS

Only actual measured values are reported:

| Metric | Value |
|---|---:|
| EI annotation rows | 24,686 |
| EI valid-label rows | 24,321 |
| EI unique prompts | 12,865 |
| EI unique PMCIDs | 3,372 |
| EI train/validation/test article IDs | 3,562 / 443 / 449 |
| Prototype clean / omission / total | 64 / 64 / 128 |
| Prototype omission heuristic accuracy | 1.000 |
| Prototype deterministic rerun byte comparison | identical |

No model accuracy, retrieval metric, selective risk, calibration, or GPU metric was computed.

## GATES

- **Novelty Closure Gate — CONDITIONAL:** no exact overlap identified, but the audit is bounded and the data gap prevents full validation.
- **Data Structure Gate — FAIL for the original full benchmark / CONDITIONAL for a narrowed study-level track:** EI supports study-level ICO/effect/span objects; MS² supports review/study structure but not verified gold cross-study direction in the inspected sample.
- **Trial-Family Gate — FAIL for the original full benchmark:** no trial-family identifiers or validated linkage are present in the inspected sources.
- **Label Semantics Gate — FAIL for full three-way semantics / PASS for the bounded omission probe:** `CONFLICT` and duplicate semantics cannot be defended from current data.
- **Perturbation Validity Gate — FAIL for the full taxonomy / CONDITIONAL for omission only:** one deterministic omission transformation is valid but trivially solvable.
- **Leakage-Control Gate — CONDITIONAL:** article-level EI split separation passes; trial-family control is unavailable.
- **Triviality Gate — FAIL for the current prototype:** evidence-count rule reaches 1.000 accuracy.
- **Reproducibility Gate — PASS:** source hashes, prototype hashes, deterministic rerun, manifests, tests, and artifact boundaries are working.

## ARTIFACTS

Tracked or intended compact artifacts:

- `PROJECT_SPEC.md`
- `docs/NOVELTY_AUDIT.md`
- `docs/DATA_FEASIBILITY.md`
- `docs/BENCHMARK_SCHEMA.md`
- `docs/PERTURBATION_SPEC.md`
- `docs/LEAKAGE_AUDIT.md`
- `docs/DATA_MANIFEST.md`
- `docs/HEURISTIC_SANITY.md`
- `docs/ROADMAP_AND_GATES.md`
- `src/trialtrace/prototype.py`
- `scripts/build_prototype.py`
- `scripts/audit_sources.py`
- `tests/unit/test_prototype.py`
- `data/manifests/milestone_1_source_manifest.json`
- `data/manifests/milestone_1_audit.json`
- `reports/MILESTONE_1_REPORT.md`

Raw archives, extracted clinical text, and generated JSONL are excluded from Git.

## TESTS / INTEGRITY

Fresh final checks:

- Python compileall: passed.
- Pytest: **4 passed**.
- Ruff: **all checks passed**.
- Git diff whitespace check: passed.
- Prototype rerun with identical source, limit, and seed: byte-identical output.
- Prototype JSONL line count: 128.
- Source archive SHA-256: `6abe0d4ec0d331834981c0171c3c79d47515761867f82f1dc6066e43863a1586`.
- Prototype JSONL SHA-256: `e6191b920433193c57a51544b282b22126b398e23c6f83bb3330dc0b5f5241c9`.

## GIT

- Branch: `main`
- Remote: `https://github.com/rohan-303/TrialTrace.git`
- Milestone 0 pushed and verified at `4081001cc52bce3cf47fccc4e70130fc81e30253` before Milestone 1 work.
- Milestone 1 commit: final commit recorded by Git after this report freeze (`feat: establish TrialTrace benchmark feasibility`).
- Push status: Milestone 0 pushed and verified; Milestone 1 commit ready to push after this report correction.
- Tag: none.

## RISKS

1. The full intended benchmark requires a new auditable source or human-verified subset with compatible multi-study evidence and underlying trial identity.
2. MedSR-Bench’s empty public state prevents complete overlap replication; future release could alter the novelty assessment.
3. The current study-level prototype’s triviality means a narrowed project would need a materially stronger answerability contract, not merely more omission examples.

## RECOMMENDED NEXT MILESTONE

Do not begin Milestone 2. Run a separately reviewed **Milestone 1R — Data/Label Redesign Feasibility** only if an auditable multi-study source or human-verified subset can be identified. Otherwise narrow TrialTrace to a study-level evidence sufficiency/abstention benchmark and drop claims about cross-study conflict, duplicate trial reports, and trial-family leakage control.
