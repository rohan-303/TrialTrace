# TrialTrace milestone roadmap and gates

## Milestones

0. **Research specification and novelty kill-test** — complete the source-backed question, threat map, data feasibility preflight, hypotheses, and gates. No large experiments.
1. **Data and benchmark construction** — acquire only eligible data, map relationships, audit trial families, implement deterministic perturbations, freeze Benchmark v0.1, and run leakage/label integrity checks.
2. **Baseline evaluation** — run answer-always, retrieval/generation, direct multi-document, transparent heuristic, and representative agent baselines under controlled budgets. Continue only if the failure mode is real.
3. **Evidence adequacy method** — only after baseline failure; develop the simplest compatible/conflict/adequacy representation and ablate against heuristics.
4. **Calibration and selective risk** — risk–coverage, calibration, abstention/conflict quality, and optional assumption-explicit conformal analysis.
5. **Full robustness study** — frozen perturbation regimes, subgroup/error analyses, compute accounting, and shift-specific degradation.
6. **Final scientific validation** — paired bootstrap intervals, ablations, reproducibility/artifact audit, and optional small human review subset.
7. **Paper and release** — paper, figures/tables, benchmark docs, system cards, limitations/ethics, README, and reproducibility instructions.

The sequence is retained. The only scope modification is that Milestone 1 must contain an explicit closest-benchmark replication/overlap audit before the benchmark is frozen.

## Project-level gates

| Gate | PASS condition | Failure response |
|---|---|---|
| Novelty | Controlled medical evidence-set shift + explicit answerability/conflict + selective risk remains distinct after MedSR-Bench and related-literature audit | Narrow to a replication/analysis paper or stop |
| Data | Legal, versioned, reproducible sources with auditable review/study/trial identities | Narrow dataset/track or stop |
| Label | Deterministic/auditable labels; unresolved cases excluded rather than guessed | Narrow label space or stop |
| Leakage | No cross-split review/trial/identifier/near-duplicate leakage | Rebuild splits; no results survive invalid split |
| Failure mode | Strong baselines degrade in scientifically meaningful, non-trivial ways | Stop method development or reframe as negative result |
| Method | Improvement over transparent heuristics at matched resources | Stop new-method claim |
| Selective risk | Reduced risk at an interpretable coverage range with uncertainty | Report only descriptive robustness if not met |
| Reproducibility | Fresh rerun, manifests, hashes, configs, and immutable outputs verify | Do not freeze/release |
| Publication | One load-bearing contribution survives all above gates | Do not force a paper claim |

## Milestone 1 decision

Milestone 1 executed a bounded EI feasibility prototype and closed the current branch as **REDESIGN_REQUIRED**. Do not begin Milestone 2. The minimum next step is a new data/label feasibility design that supplies audited multi-study compatible evidence and trial-family identities; otherwise narrow the project to study-level sufficiency/abstention and drop conflict/duplicate claims.

Milestone 0–1 compute: local CPU only for repository checks, metadata inspection, schema profiling, hashing, and deterministic tests. No remote GPU use was needed.

Milestone 2 onward: use the authorized dual-RTX-4090 SSH server only after environment inspection and explicit compute authorization. Use one GPU unless parallelism is justified; record GPU/CUDA/model/precision/batch/memory metadata. Keep local repository authoritative, transfer only manifest-listed files, hash-check results on return, and delete only the user-created remote workspace. Never transfer credentials, private keys, restricted raw data, or model caches.

## Risks most likely to kill publication value

1. **Benchmark overlap:** MedSR-Bench or a related benchmark may already encode the same evidence-set robustness/answerability problem. This is the highest-priority kill test.
2. **Trial identity and label validity:** publication-level metadata may not support underlying-trial deduplication or deterministic cross-study conflict labels. A benchmark that confuses reports with trials would be scientifically weak.
3. **Triviality/realism:** systems may fail only because of crude retrieval degradation or synthetic perturbations, while simple count/direction/coverage rules match the proposed method. The benchmark must include realistic, auditable shifts and strong transparent baselines.
