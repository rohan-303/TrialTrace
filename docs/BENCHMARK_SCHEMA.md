# TrialTrace benchmark schema status

## Milestone 1R result

The rescued multi-study schema is **not instantiated**. TrialReviewBench provides review/question records and included publication records, while the public ED-Trials interface exposes trial/publication metadata and thread concepts. A reproducible cross-source trial-family graph was not frozen because the legacy Epistemonikos API requires a registered access token and the current public frontend API did not expose a documented bulk export or stable thread endpoint during this milestone.

The schema below is therefore a **conditional contract**, not a generated benchmark and not evidence that the sources can be joined at scale.

## Conditional canonical hierarchy

```text
review_question
  review_id
  question_id
  source_review_identifiers[]
  pico
  included_trial_families[]
    trial_family_id
    identity_status
    reports[]
      report_id
      pmid
      pmcid
      doi
      registry_ids[]
      source
      source_revision
      provenance
    outcomes[]
      outcome_id
      normalized_name
      source_name
      effect_direction
      effect_estimate
      uncertainty
      evidence_source
```

## Required identity distinctions

- `report_id` identifies a publication or registry record, never automatically an underlying trial.
- `trial_family_id` may be assigned only from an explicit source relationship or an auditable human-verified linkage record.
- A publication thread is a candidate trial-family proxy, not automatically a ground-truth trial family. Protocols, preliminary reports, final reports, subgroup analyses, and follow-ups must be audited before use.
- `review_id` and `question_id` are distinct: one review may contain multiple evidence questions or outcomes.
- Every derived relationship carries source, revision, retrieval time, transformation, and confidence/status provenance.

## Semantics required for a future benchmark

`D(q,E) ∈ {SYNTHESIZE, CONFLICT, ABSTAIN}` must be derived from a frozen evidence contract, not from document count or an LLM judgment.

- `SYNTHESIZE`: compatible, independently supported trial-family evidence satisfies the contract and preserves the benchmark conclusion.
- `CONFLICT`: compatible independent trial families support materially different directions or conclusions under the same outcome/PICO contract.
- `ABSTAIN`: evidence is present but fails the contract because of missing decisive families, PICO incompatibility, duplicate-only support, insufficient independent support, or another explicitly recorded reason.
- `UNRESOLVED`: identity, compatibility, or outcome semantics are not auditable. Unresolved instances must be excluded from the three-way target rather than forced into a label.

## Current available schemas

### TrialReviewBench

- `reviews.csv`: 100 review records with `PMID`, title, abstract, PICO, and topic.
- `study-search-screening.jsonl`: 100 review records with `Involved_Citations`; each citation can contain title, `pmid`, `doi`, `nctid`, and PDF link.
- `data-extraction/*.csv`: 23 review-specific CSVs with heterogeneous columns and 632 rows. The public dataset viewer reports a schema-cast failure because files do not share one column schema.
- No explicit `trial_family_id`, publication-thread identifier, or cross-review trial graph is present in the inspected release.

### Evidence Inference 2.0 / MS²

The prior study-level and review-level schemas remain historical feasibility probes. They do not acquire trial-family identity through this milestone.

## Release rule

A future v0.2 benchmark may release identifiers, hashes, transformations, labels, and linkage evidence while requiring users to rehydrate source text from authorized APIs. Raw full text and restricted records remain outside Git and outside any release until rights are verified.
