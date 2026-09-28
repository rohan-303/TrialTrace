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
