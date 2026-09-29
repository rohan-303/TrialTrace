# Milestone 1R report

## MILESTONE

**Milestone 1R — Multi-Study Data and Label Rescue Test**

Scope was limited to source access, schema inspection, bounded cross-source feasibility, label-contract design, and release feasibility. No LLM baseline, model training, fine-tuning, GPU experiment, or method development was performed.

## MASTER DECISION

# PARTIAL_REDESIGN_REQUIRED

TrialReviewBench rescues a usable review/question → included-report → structured-extraction backbone, but the original trial-family-aware TrialTrace benchmark is not recovered. Epistemonikos exposes the right conceptual objects—review evidence structures, publication/study threads, and trial records—but the auditable, reproducible access path required for a benchmark-scale thread graph was not established in this milestone. Trial-family identity therefore cannot be claimed for the inspected TrialReviewBench records.

The surviving research question is narrower:

> Can evidence-synthesis systems preserve or appropriately reject review-level conclusions when deterministic, provenance-preserving evidence-set perturbations are applied to a multi-report clinical evidence collection with structured PICO and outcome metadata?

This surviving question must drop any unverified claim of trial-family deduplication, independent-trial conflict, or trial-family leakage control unless a separately human-verified subset is created.

## SOURCE AUDIT

### Epistemonikos / ED-Trials

The legacy Epistemonikos API documentation states that document, matrix, and studies-thread endpoints exist, but also states that the beta API requires a registered client access token. Direct unauthenticated requests to the documented document and studies-thread endpoints returned HTTP 401 (`Not Authorized`). No token was guessed, reused, or requested through chat.

The current public ED-Trials website is accessible and identifies a frontend API base at `https://api.iloveevidence.com/v2.1`. A bounded public POST request to `/references/search` returned reference records with report identifiers, DOI/PubMed links, registry fields, and a `threads` field. However, the frontend route is not a documented bulk benchmark export, its query contract is not frozen for this project, and the bounded request did not yield a reproducible review-to-thread graph for the TrialReviewBench records.

The ED-Trials methods page documents continuously updated search sources, deduplication/quality assurance, study selection, automated/semi-automated methods, and human validation. The public site therefore supports feasibility investigation, but not automatic acceptance of its thread IDs as gold trial-family IDs. A publication thread remains a candidate proxy that requires audit of protocols, preliminary reports, final reports, subgroup analyses, follow-ups, and extensions.

### TrialReviewBench

The release was downloaded from the official Hugging Face dataset repository at the pinned main-branch commit `6dfc322004341212eb905a6874ccfae416b9f9f5`.

Measured release contents:

- `TrialReviewBench-reviews.csv`: **100** review rows;
- `TrialReviewBench-study-search-screening.jsonl`: **100** review rows;
- included citation records: **2,220**;
- distinct included PMIDs: **2,132**;
- included records with PMID: **2,132 / 2,220 = 96.036%**;
- distinct non-empty DOI values: **25**;
- included records with non-empty DOI: **25 / 2,220 = 1.126%**;
- distinct non-empty NCT identifiers: **11**;
- included records with non-empty NCT identifier: **11 / 2,220 = 0.495%**;
- review citation-set size: minimum **1**, mean **22.2**, maximum **150**;
- data-extraction files: **23**;
- data-extraction rows: **632**;
- distinct extraction PMIDs: **477**;
- extraction rows with PMID: **477 / 632 = 75.475%**;
- extraction PMIDs also appearing in the included-citation PMID set: **432**.

The release contains PICO objects in the screening JSONL and manually checked study-characteristic/result extraction files. The extraction CSVs are review-specific rather than one common schema. Their union contains heterogeneous field names, and the public dataset viewer reports a `DatasetGenerationCastError` because the files do not share one schema. This is an engineering limitation, not a reason to silently coerce fields into a common outcome ontology.

The release contains no explicit `trial_family_id`, publication-thread identifier, or cross-review trial graph in the inspected files. PMIDs identify reports, not underlying trials. The 2,220 figure is therefore a report/citation count for this audit, not a count of independent trials.

## LINKAGE RESULT

The required exact-identifier hierarchy was applied conceptually as PMID → DOI → PMCID → registry ID → source-specific ID. TrialReviewBench supplied PMID for most included records, but no stable, documented bulk endpoint was found that could return ED-Trials thread membership for the complete set without an authenticated legacy token or reverse-engineering an unstable frontend contract.

| Linkage field | Numerator | Denominator | Status |
|---|---:|---:|---|
| TrialReviewBench reports examined | 2,220 | 2,220 | VERIFIED |
| TrialReviewBench reports with PMID | 2,132 | 2,220 | VERIFIED |
| TrialReviewBench reports with DOI | 25 | 2,220 | VERIFIED |
| TrialReviewBench reports with registry ID | 11 | 2,220 | VERIFIED |
| Reports mapped into ED-Trials | NOT COMPUTED | 2,220 | BLOCKED by access/query contract |
| Reports assigned an ED-Trials thread | NOT COMPUTED | mapped reports | BLOCKED |
| Reports mapped to a review in ED-Trials | NOT COMPUTED | mapped reports | BLOCKED |
| Reports with usable structured result labels | 632 extraction rows | 2,220 reports | PARTIAL, review-specific |
| Ambiguous fuzzy matches accepted | 0 | — | VERIFIED; fuzzy assignment was not used |

No fuzzy title linkage was promoted. No zero-coverage claim is made: the ED-Trials mapping denominator could not be executed under a stable, auditable access contract.

## TRIAL-FAMILY VALIDATION

No 30–50-thread manual audit was completed because no reproducible thread sample could be obtained through the documented authenticated API without credentials. The validation sample is therefore **0**, not a negative accuracy result.

What is verified:

- Epistemonikos explicitly describes publication threads as groups of references associated with one study.
- The legacy API documentation exposes thread retrieval and document-to-thread fields.
- The current public ED-Trials frontend returns a `threads` field in reference records.

What remains unverified:

- thread completeness for TrialReviewBench PMIDs;
- whether every thread corresponds to one underlying randomized trial;
- handling of protocol/final-report pairs, subgroup analyses, extensions, and multi-phase studies;
- one-publication-to-multiple-thread ambiguity;
- thread error rate on a preregistered sample.

Consequently, `trial_family_id = thread_id` is prohibited in the current benchmark.

## MULTI-STUDY STRUCTURE

The source supports a report-level multi-study structure:

- viable review records: **100**;
- viable review/question JSONL records: **100**;
- included report/citation records: **2,220**;
- review sets with at least two included report records: **NOT RECOMPUTED as an independent-trial count**;
- independent trial families: **NOT COMPUTED**;
- report-level structured extraction rows: **632**;
- outcome-direction labels normalized across reviews: **0 frozen**;
- review-level effect conclusions suitable as deterministic TrialTrace labels: **0 frozen**.

The report-level structure is sufficient to design a bounded review-set perturbation track. It is not sufficient to claim independent-trial contradiction or duplicate-publication semantics.

## LABEL SEMANTICS

The following contract is objectively supportable only after an additional deterministic outcome-normalization and review-level conclusion specification:

- `SYNTHESIZE`: retained reports satisfy the frozen PICO/report inclusion contract and preserve a reference review-level result under a defined structured-result rule.
- `CONFLICT`: retained, PICO-compatible **independently identified trial families** support materially different directions. This label is currently unsupported because trial-family identity and common outcome direction are not frozen.
- `ABSTAIN`: evidence is present but fails a predeclared contract, such as missing decisive report groups, wrong PICO dimension, duplicate-only support, insufficient structured-result coverage, or unresolved identity.
- `UNRESOLVED`: source identity, outcome compatibility, or result semantics cannot be audited. These rows must be excluded from three-way scoring.

`ABSTAIN` is explicitly not equivalent to an empty evidence set. However, a non-trivial abstention label requires a frozen evidence contract and matched counterexamples; it cannot be assigned merely because a perturbation was named “omission.”

Candidate contracts evaluated conceptually:

- directional support preservation;
- material review-conclusion preservation;
- minimum independent-trial support;
- PICO compatibility completeness.

Only the first two appear potentially derivable from selected TrialReviewBench review tables, and neither was frozen because the available extraction schemas are heterogeneous and no common outcome ontology was established. The independent-trial and compatibility-completeness contracts remain blocked without additional linkage/annotation.

## RESCUED PROTOTYPE

**Not created.** The source audit did not justify emitting a TrialTrace Prototype v0.2 with three-way labels. Creating one would require either pseudo-labels or unverified thread assignments.

The downloaded TrialReviewBench files and machine-readable audit are source-feasibility artifacts, not a benchmark release. The previous one-report EI prototype remains historical and invalid for the multi-study target; it was not expanded.

## TRIVIALITY / METADATA BASELINES

No scientific benchmark labels were frozen, so no metadata classifier accuracy was computed. The following baseline risks were identified and must be tested before any future prototype:

- included report count and review size;
- number of reports with structured extraction rows;
- PMID/DOI/NCT missingness;
- extraction-file identity and topic;
- perturbation type;
- lexical PICO overlap;
- number of distinct trial-family IDs, once independently verified;
- direction majority, once a common outcome ontology exists.

The prior EI evidence-count heuristic remains a failed historical gate: it achieved 1.000 on the one-report omission prototype. It is not evidence about TrialReviewBench.

## COUNTERFACTUAL PAIRS

**Count: 0 constructed.** No pairs were generated because the label contract and trial-family/outcome semantics were not frozen. Future pairs must match approximate report count, metadata missingness, and document-length distributions while differing in the evidence-supported decision; perturbation type alone must never determine the target.

## NOVELTY RESULT

The rescue audit does not establish strong novelty. TrialReviewBench already supplies a multi-review clinical evidence-synthesis benchmark with study search, screening, and extraction tasks, and the associated work reports manually checked study relationships and structured characteristics/results. The surviving distinction is narrower and conditional: deterministic perturbation of retained evidence sets with explicit answerability semantics and selective evaluation, provided labels are derived from audited structured results rather than report count.

Epistemonikos is a plausible structural complement because it exposes publication/study-thread concepts, but the source audit did not verify a usable TrialReviewBench-to-thread graph. Therefore the project must not claim trial-family-aware novelty or successful deduplication.

## LICENSE / RELEASE RESULT

- TrialReviewBench dataset card declares Apache-2.0; the exact pinned release commit and file hashes are recorded in the audit artifact.
- The TrialMind paper states that study full content was retrieved under PubMed policy; this does not automatically grant unrestricted redistribution of all underlying article text.
- ED-Trials is publicly searchable and displays Terms of Service/Privacy Policy links, but the legacy API requires a registered access token and the current frontend API terms/export contract were not established as a benchmark redistribution license.
- A defensible release path would publish identifiers, pinned source revisions, hashes, deterministic transforms, exclusions, labels, and linkage evidence, while requiring rehydration from authorized sources. Raw full text and restricted records must remain outside Git.
- Release licensing is **CONDITIONAL** until ED-Trials access and derived-thread redistribution terms are confirmed with the provider.

## GATES

- **Multi-Study Structure Gate — PASS for report-level structure / CONDITIONAL for independent-trial structure:** 100 review records and 2,220 included report records are available; independent-trial counts are not established.
- **Trial-Family Identity Gate — FAIL for the original claim:** no verified TrialReviewBench thread graph or audited thread sample was obtained.
- **Outcome/Direction Gate — CONDITIONAL:** 632 heterogeneous extraction rows exist, but no common direction ontology or frozen review-level result label was created.
- **Three-Way Label Gate — FAIL for the original semantics / CONDITIONAL for a narrower review-conclusion contract:** conflict and duplicate labels are unsupported; answerability may be possible only with additional structured-result specification.
- **Perturbation Gate — CONDITIONAL:** report-set perturbations are technically possible; trial-family omission, duplicate amplification, and independent directional omission are not currently defensible.
- **Triviality Gate — NOT PASSED:** no new labels were frozen, so the gate was not executed. The historical one-report prototype failed this gate.
- **Counterfactual Gate — FAIL:** zero matched pairs were constructed.
- **Leakage Gate — FAIL for trial-family control / CONDITIONAL for report-level control:** PMID-based report grouping is available; trial-family leakage cannot be audited.
- **Licensing Gate — CONDITIONAL:** TrialReviewBench has a declared dataset license; ED-Trials API and derived-thread release terms remain unresolved.
- **Novelty Gate — CONDITIONAL:** a narrower perturbation/answerability evaluation may remain distinct from TrialReviewBench, but trial-family-aware novelty is not supported.

## ARTIFACTS

- `scripts/audit_rescue_sources.py` — deterministic TrialReviewBench schema/count/hash audit.
- `artifacts/milestone_1r/20260929_source_rescue/trialreviewbench_audit.json` — machine-readable counts, coverage, schemas, source hashes, and limitations.
- `artifacts/milestone_1r/20260929_source_rescue/trialreviewbench/` — local downloaded source files, excluded from Git.
- `docs/BENCHMARK_SCHEMA.md` — conditional rescued schema and explicit non-claims.
- `docs/NOVELTY_AUDIT.md` — to be updated with the rescue result.
- `docs/DATA_FEASIBILITY.md` — to be updated with source and licensing findings.

## TESTS / INTEGRITY

Fresh final checks completed after the final document edit:

- source download completed for all 26 TrialReviewBench files;
- HF main revision resolved to `6dfc322004341212eb905a6874ccfae416b9f9f5`;
- audit script executed successfully;
- 100 review rows, 100 screening rows, 2,220 citation records, 23 extraction files, and 632 extraction rows measured from disk;
- audit JSON contains per-file hashes for downloaded source files;
- no fuzzy linkage or generated labels were written;
- no models, checkpoints, predictions, or GPU outputs were created;
- compilation: passed;
- pytest: **5 passed**;
- Ruff: **all checks passed**;
- Git whitespace check: **passed**.

## GIT

- Branch: `main`.
- Starting commit: `584ed328c13418ccbc5cc77fcfc12485cebacb35`.
- Remote: `https://github.com/rohan-303/TrialTrace.git`.
- Push status before this milestone: local and remote `main` matched at the starting commit.
- Target commit message: `feat: evaluate multi-study TrialTrace redesign`.
- Tag: none planned.
- Worktree status: to be verified after final edits and commit.

## RISKS

1. The original trial-family-aware benchmark still depends on authenticated or otherwise unstable ED-Trials access plus a 30–50-thread manual validation study.
2. TrialReviewBench’s heterogeneous review-specific extraction schemas may require a human-audited common outcome ontology before labels are defensible.
3. Even a report-level perturbation benchmark may be too close to existing TrialReviewBench unless the selective answerability target reveals failures not measured by search, screening, and extraction metrics.

## RECOMMENDED NEXT MILESTONE

Do not begin Milestone 2. The next reviewed milestone should be either:

- **Milestone 1S — Narrow Review-Level Label Feasibility:** freeze a small human-verified subset and a common structured-result contract, then test counterfactual/triviality gates without trial-family claims; or
- terminate the TrialTrace line if human verification and ED-Trials access cannot be authorized.
