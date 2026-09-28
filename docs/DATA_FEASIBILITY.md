# Data-source and schema feasibility preflight

## MS² / MSLR2022

**Verified from official README:** MS² contains medical systematic reviews, constituent studies, and related markup; it is an annotated subset of the Semantic Scholar research corpus. The README directs users to the MSLR2022 Shared Task cleaned data and states that the original data is under the Semantic Scholar API and Dataset License Agreement.

**Potential value:** review-to-constituent-study grouping and multi-document context are directly relevant to evidence-set construction.

**Feasibility risks:**

- the license is not equivalent to unrestricted PMC OA reuse;
- constituent links may be publication-level rather than underlying-trial-level;
- effect direction/PICO compatibility may be absent or heterogeneous;
- review inclusion criteria and review conclusions may not provide deterministic `SYNTHESIZE/CONFLICT/ABSTAIN` labels;
- the original repository is old and points to a later shared-task release, so version pinning is mandatory.

**Milestone 1 checks:** retrieve the authoritative shared-task manifest, preserve release identifiers and terms, inspect JSON/schema examples, count review/study links, map PMIDs/DOIs, and quantify unresolved trial-family identity.

## Evidence Inference 2.0

**Verified from official README/paper:** articles describe randomized clinical trials; prompts ask about intervention vs comparator with respect to an outcome; labels represent significantly increased, decreased, or no significant effect; supporting evidence spans are provided; raw documents are distributed in PubMed NXML and plain text forms; annotations are distributed as CSV with JSON conversion support. The 2.0 paper reports additional annotations, stronger baselines, quality inspection, and an abstract-only version.

**Potential value:** study-level direction and evidence-span supervision; a natural source for clean evidence units, PICO mismatch checks, and directionally contradictory study sets.

**Feasibility risks:**

- article-level prompts do not automatically establish cross-study compatibility;
- “no significant effect” is not proof of equivalence or absence of clinically meaningful effect;
- the repository is MIT, but the article/text data has separate provenance and licensing terms;
- trial-family identity, registry identifiers, and duplicate-publication relationships require independent audit;
- the public download endpoint and current schema must be verified before acquisition.

## PMC Open Access

Use only article-level OA-eligible material with source identifier, license text, retrieval date, and SHA-256 in a manifest. Do not assume that a PMC record implies identical reuse rights. Restricted, missing-license, or ambiguous material is excluded or retained only as an external identifier without text.

## Milestone 1 audit results

The official EI v2.0 archive was acquired and inspected. It contains 24,686 annotation rows, 24,321 valid-label rows, 12,865 unique prompts, 3,372 PMCIDs, and disjoint article-level train/validation/test files with 3,562/443/449 IDs. PMCID is available; DOI, trial-registration, and trial-family fields are absent. The current archive also contains 619 valid rows with `significantly increase`, inconsistent with the documented `significantly increased`; these were excluded from the prototype.

The official MS² sample contains one review with 20 included reports, all with PMIDs but no DOIs or trial-registration identifiers. Its significance fields are not treated as verified gold cross-study direction labels. The larger MSLR2022 archive is documented as approximately 253 MB and approximately 20K reviews/470K studies, but was not downloaded during this bounded milestone.

**Data Structure Gate:** FAIL for the original full benchmark; CONDITIONAL for a narrowed study-level track. The current sources do not support verified trial-family grouping or deterministic multi-study conflict labels.

## Required manifest fields

`source_name`, `source_version`, `source_url`, `download_date`, `license_url`, `license_status`, `raw_filename`, `sha256`, `pmid`, `doi`, `trial_registration_id`, `review_id`, `study_id`, `trial_family_id`, `document_type`, `pico_fields`, `effect_direction`, `evidence_span_ids`, `parent_set_id`, `perturbation_type`, `seed`, `split`, `eligibility_status`, `notes`.

## Provisional labels

Do not construct labels from generated prose. Candidate deterministic labels must be defined from compatible study metadata, direction/effect annotations, source-set membership, and perturbation operations. Ambiguous instances are a separate `UNRESOLVED` pool and must not be forced into the three-way target.
