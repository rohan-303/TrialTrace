# Milestone 0 novelty and feasibility audit

**Cutoff:** 2026-09-28 (UTC/US-Eastern retrieval session)
**Evidence status:** targeted primary-source audit, not a systematic review. Search failures and unresolved identities are recorded as uncertainty rather than negative findings.

## Executive decision

**Master decision: CONDITIONAL — proceed to Milestone 1 only after external review, with a narrowed claim.**

The central idea survives as a plausible benchmark/evaluation gap, not as an established novel method: the inspected systems emphasize retrieval, screening, extraction, citation-grounded synthesis, or contradiction finding, while TrialTrace proposes controlled *evidence-set corruption* with explicit `SYNTHESIZE / CONFLICT / ABSTAIN` decisions and selective risk–coverage evaluation. This distinction is not yet proven unique. The strongest threats are TrialMind/MedSR-Bench on medical evidence-synthesis benchmarking, PaperQA2 on contradiction detection, and the broader abstention/calibration literature.

No empirical project result has been computed. The project should not claim that current systems fail until Milestone 2 executes controlled baselines.

## Direct comparison

| Work | Verified emphasis | Overlap | Current distinction / threat |
|---|---|---|---|
| MedSR-Copilot / MedSR-Bench | PRISMA-aligned multi-agent retrieval, screening, extraction, risk-of-bias, and statistical synthesis; traceable intermediate artifacts | Medical systematic-review workflow, benchmarked components, evidence synthesis | The repository describes a broad workflow, not yet a controlled corruption benchmark or selective adequacy decision. This is the strongest direct threat because benchmark semantics and robustness may overlap. Must inspect the dataset cards/paper before keeping the central claim. |
| OpenScholar | Retrieval-augmented scientific QA over a 45M open-access corpus; ScholarQABench evaluates long-form cited answers | Retrieval, scientific synthesis, citations, biomedical queries | OpenScholar measures answer correctness/citation quality, not a medical trial-family evidence-set corruption protocol or explicit abstention/conflict state. It remains a strong answer-quality baseline. |
| PaperQA2 | Agentic scientific search/synthesis; LitQA2 and human comparison; reported contradiction identification | Retrieval, citation-backed synthesis, contradiction discovery | Contradiction detection is a direct overlap with `CONFLICT`, but the inspected work is not the same as controlled omission/mismatch/duplication benchmark plus selective risk-coverage decision. TrialTrace must compare on contradiction and citation-faithfulness, not imply PaperQA2 lacks conflict capability. |
| TrialMind / TrialReviewBench | Search, screening, and extraction for clinical evidence synthesis; 100 reviews and 2,220 studies in the cited abstract | Clinical-review benchmark, study-set construction, screening/extraction | TrialMind is closer to workflow acceleration and recall/accuracy than pre-synthesis adequacy under evidence-set shift. It is a required baseline/threat; TrialTrace must avoid reproducing its benchmark framing. |
| LEADS | Exact work could not be uniquely identified in bounded primary-source searches | Possible systematic-review automation overlap | Do not assert details. Resolve the exact citation supplied by the project owner or external reviewer before using LEADS as evidence. |
| Recent medical systematic-review agents | Broadly include retrieval, eligibility screening, extraction, RoB, meta-analysis, and human-in-the-loop review | Medical evidence workflow and auditability | Most apparent overlap is pipeline function, while TrialTrace’s surviving question is robustness of the evidence *set* and selective answerability. This must be verified against a broader structured review before publication claims. |
| Selective prediction / abstention for RAG | Confidence, calibration, refusal, and risk-coverage methods | Abstention and selective risk | TrialTrace cannot claim abstention or risk-coverage as new. The candidate contribution is the clinical evidence-set shift protocol and the decision semantics, if they are shown to reveal failures missed by standard metrics. |
| Provenance-aware scientific QA | Citation entailment, evidence spans, source attribution, and faithfulness | Provenance and grounding | Provenance is a necessary control, not the load-bearing novelty. TrialTrace tests whole-set adequacy beyond individually supported claims. |

## What survives

A narrow, falsifiable contribution remains plausible:

> A deterministic benchmark protocol for testing whether medical evidence-synthesis systems preserve answerability, expose cross-study conflict, and abstain under clinically meaningful evidence-set corruptions, evaluated with selective risk at controlled evidence and compute budgets.

This is a benchmark/evaluation contribution first. A new adequacy model is not justified until baseline failure is demonstrated.

## What does not survive as a standalone claim

- “First medical evidence-synthesis agent with abstention.”
- “Novel citation or provenance method.”
- “Novel contradiction detection.”
- “Conformal guarantees under evidence-set shift.”
- “Another complete systematic-review agent.”
- “Combining existing datasets, perturbations, and metrics is automatically novel.”

## Open kill tests

1. Read the MedSR-Bench dataset card and primary paper; determine whether its task already contains controlled incomplete/conflicting evidence and answerability labels.
2. Reproduce the exact evaluation object and perturbation semantics of the closest benchmark, if available.
3. Verify trial-family and review-family identifiers in both candidate datasets.
4. Establish whether deterministic ground truth can be derived without using model-generated labels.
5. Run a tiny, non-scientific schema feasibility probe in Milestone 1 before acquiring large text.

## Sources and evidence

- MS² official repository and README: https://github.com/allenai/ms2 and https://raw.githubusercontent.com/allenai/ms2/master/README.md. The README identifies systematic reviews, constituent studies, related markup, the MSLR2022 migration, and Semantic Scholar licensing.
- MS² dataset paper: https://arxiv.org/abs/2104.06486. Retrieved access was rate-limited in this session; metadata remains to be verified from an alternate authoritative route.
- Evidence Inference official repository: https://github.com/jayded/evidence-inference and README: https://raw.githubusercontent.com/jayded/evidence-inference/master/README.md. The README describes RCT articles, PICO-like prompts, direction labels, evidence spans, and an Evidence Inference 2.0 note.
- Evidence Inference 2.0 paper: https://arxiv.org/abs/2005.04177. The abstract states that the task infers comparative treatment performance from a trial article and identifies supporting evidence; it also reports a 25% data expansion and an abstract-only version.
- OpenScholar: https://arxiv.org/abs/2411.14199.
- PaperQA2 / LitQA2: https://arxiv.org/abs/2409.13740.
- TrialMind / TrialReviewBench: https://arxiv.org/abs/2406.17755.
- MedSR-Copilot official repository: https://github.com/MAGIC-AI4Med/MedSR-Copilot; README and linked MedSR-Bench card: https://huggingface.co/datasets/halfmorepiece/MedSR-Bench.

The MedSR-Copilot paper identity, benchmark card, LEADS identity, and the full selective-RAG/provenance literature map remain **open/partially verified**, not negative findings.

## Milestone 1 closure update

**Novelty Closure Gate: CONDITIONAL / REDESIGN REQUIRED.**

The central framing remains differentiated enough to justify a narrowed benchmark study, but the current data cannot instantiate the full contribution. The bounded audit supports this cautious statement:

> The inspected closest systems establish medical review workflow automation, study-level extraction, citation-backed scientific synthesis, or contradiction discovery. The exact combination of deterministic clinical evidence-set corruption, explicit `SYNTHESIZE / CONFLICT / ABSTAIN` semantics, trial-family leakage controls, and selective risk–coverage evaluation was not found in the bounded primary-source audit. This is an unresolved gap, not a proof of novelty.

MedSR-Copilot/MedSR-Bench is a direct overlap threat, but its public Hugging Face dataset currently states that it is empty and its repository README marks the paper as “coming soon.” This weakens—but does not eliminate—the threat.

### Final overlap matrix

Legend: **E** = established/explicit; **P** = partial or adjacent; **U** = unresolved/not verified; **—** = not the primary object.

| Work / direction | Multi-study clinical synthesis | Review vs study | PICO | Provenance | Effect direction | Conflict | Missing evidence | PICO mismatch | Duplicate reports | Answerability | Abstention | Selective risk | Deterministic corruption | Trial-family control | Trajectories |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **TrialTrace target** | E | both | E | E | E | E | E | E | E | E | E | E | E | E | P |
| MedSR-Copilot / MedSR-Bench | E | review/workflow | E | E | P | P | U | P | U | U | U | U | U | U | E |
| TrialMind / TrialReviewBench | E | review/workflow | E | P | P | — | — | P | U | — | — | — | — | U | P |
| OpenScholar / ScholarQABench | P | mixed QA | P | E | — | P | — | — | — | — | — | P | — | — | P |
| PaperQA2 / LitQA2 | P | literature QA | P | E | — | E | — | — | — | — | — | P | — | — | E |
| Evidence Inference 2.0 | — | study-level | E | E | E | — | — | — | — | — | — | — | — | — | — |
| MS² / MSLR2022 | E | review-level | P | P | U | — | — | — | — | — | — | — | — | U | — |
| selective RAG / abstention | P | usually QA | P | P | — | P | P | P | — | P | E | E | P | — | P |
| provenance-aware scientific QA | P | literature QA | P | E | — | P | P | P | — | P | P | P | P | — | P |

This matrix is a design audit, not an exhaustive systematic review.

### Findings by contribution dimension

**Established:** medical systematic-review workflow automation; citation-backed scientific synthesis; contradiction discovery; study-level intervention/comparator/outcome direction and evidence spans; abstention and risk–coverage methodology.

**Incremental alone:** adding a `CONFLICT` label; adding provenance/evidence spans; combining MS² and Evidence Inference; listing omission/mismatch perturbations without non-trivial labels and trial identities.

**Apparently underexplored:** a source-grounded medical benchmark where deterministic evidence-set corruption requires synthesize/conflict/abstain decisions, evaluated by whole-set selective risk and explicitly separated report/trial-family identity. These are potentially novel benchmark directions, not confirmed novelty.

**Uncertain:** hidden MedSR-Bench task semantics; recent 2025–2026 systems outside the inspected endpoints; the exact intended LEADS work; availability of legally usable multi-study trial-linked data.

### Source-backed closure record

- MedSR-Copilot repository: https://github.com/MAGIC-AI4Med/MedSR-Copilot (README accessed 2026-09-28).
- MedSR-Bench public dataset page: https://huggingface.co/datasets/halfmorepiece/MedSR-Bench (currently empty, accessed 2026-09-28).
- TrialMind / TrialReviewBench: https://arxiv.org/abs/2406.17755.
- OpenScholar / ScholarQABench: https://arxiv.org/abs/2411.14199.
- PaperQA2 / LitQA2: https://arxiv.org/abs/2409.13740.
- Evidence Inference 2.0 and official download page: https://arxiv.org/abs/2005.04177 and https://evidence-inference.ebm-nlp.com/download/.
- MS² / MSLR2022: https://github.com/allenai/ms2 and https://github.com/allenai/mslr-shared-task.
- LEADS: exact identity unresolved; no substantive claims are made.

### Minimum redesign

1. Treat the EI prototype as a data/engineering feasibility probe only.
2. Do not claim multi-study conflict, duplicate-report, or PICO-distractor support until independent trial-family and compatibility relations are obtained.
3. Add an auditable source or human-verified subset with compatible multi-study evidence units and underlying trial identity.
4. If that source cannot be obtained, narrow the project to study-level evidence sufficiency/abstention and explicitly drop conflict and duplicate-family claims.

## Milestone 1R rescue closure

The Epistemonikos/ED-Trials rescue audit did not establish trial-family-aware feasibility. The legacy API documents study-thread endpoints but requires a registered access token; unauthenticated requests returned HTTP 401. The current public frontend exposes a public references-search API and thread fields, but no stable, documented bulk linkage contract was frozen. No thread sample was therefore audited, and no thread ID was promoted to `trial_family_id`.

TrialReviewBench was downloaded and measured at 100 review records, 2,220 included report records, 2,132 PMID-bearing records, 25 DOI-bearing records, 11 NCT-bearing records, 23 heterogeneous extraction files, and 632 extraction rows. It provides a useful report-level review/question backbone, but no explicit trial-family graph or common cross-review outcome ontology. The dataset already covers clinical evidence-synthesis search, screening, and extraction, so a future TrialTrace contribution must be narrower than a general evidence-synthesis benchmark.

**Updated novelty statement:** a report-level benchmark for deterministic evidence-set perturbation and selective answerability may remain conditionally differentiated from TrialReviewBench, but the stronger claim involving audited independent trial families, duplicate-publication perturbations, and trial-family leakage control is not supported. No three-way labels, counterfactual pairs, or rescued prototype were generated in Milestone 1R.

Source audit artifact: `artifacts/milestone_1r/20260929_source_rescue/trialreviewbench_audit.json` (ignored local artifact).

## Milestone 1S novelty reset and closure

The candidate formulation was narrowed to paired review-level conclusion stability under controlled evidence-set perturbation. Three closer threats were explicitly added:

- **Evidence Sufficiency Benchmark**, Zhang and Wu, DOI `10.32604/cmc.2026.086343`: evaluates full, partial, irrelevant, absent, and conflicting evidence with answer/abstain behavior, evidence-sufficiency curves, and over-answering. Generic evidence sufficiency, abstention, and selective calibration are not TrialTrace novelty.
- **MetaSyn**, arXiv `2606.17041`: provides expert-curated meta-analyses, PI/ECO criteria, included studies, hard negatives, PubMed-linked corpora, and stage-wise retrieval/screening/synthesis evaluation. PICO-aware retrieval and hard-negative screening are not sufficient novelty.
- **An auditable evidence compiler for large language model-assisted systematic reviews**, Yin, Jing, and Zhang, DOI `10.64898/2026.09.21.26363538`: links evidence identities, populations, outcomes, statistical roles, dependence/overlapping participants, corrections, supersession, deterministic statistics, terminal refusal states, and auditable releases. Provenance and deterministic compilation alone are not sufficient novelty.

TrialMind/TrialReviewBench, MedSR-Copilot/MedSR-Bench, and recent numerical meta-analysis extraction benchmarks remain adjacent or direct workflow threats. The counterfactual object is conceptually distinct, but the Milestone 1S source audit found only three strict quantitative review/outcome units, 28 parseable HR records, zero leave-one-out transitions, and one non-preserving multi-report pair. A report-count rule perfectly identified the only transition. The candidate therefore fails the non-triviality and counterfactual gates, and no positive novelty claim is retained.

**Milestone 1S novelty result: CONDITIONAL in concept, FAIL as an executable benchmark on the frozen source. Master project decision: `TRIALTRACE_STOP`.**
