# Milestone 1 heuristic sanity check

The bounded prototype contains one clean valid EI prompt per instance and a paired version with its sole report omitted. A rule that predicts `SYNTHESIZE` when `evidence_set` is non-empty and `ABSTAIN` otherwise achieved **1.000 accuracy over 128 prototype rows**.

This is not evidence of a successful TrialTrace method. It is a benchmark warning: the current omission probe exposes its answerability label directly through evidence count. The result supports `REDESIGN_REQUIRED`, not `BENCHMARK_READY`.

A meaningful benchmark must contain independently audited compatible evidence sets, legitimate conflicts, incomplete-but-nonempty sets, and PICO-incompatible distractors so that answerability cannot be read from one metadata bit.
