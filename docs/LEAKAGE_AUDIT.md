# Leakage and identity audit — Milestone 1

## Evidence Inference 2.0

Measured from the retrieved v2.0 archive:

- 24,686 annotation rows.
- 24,321 rows with `Valid Label=True`.
- 12,865 unique prompts.
- 3,372 unique PMCIDs.
- Source split files contain 3,562 train, 443 validation, and 449 test article IDs.
- Pairwise intersections among train/validation/test article-ID files: 0, 0, 0.
- Prompt rows per article: maximum 72.
- PMCID is present; DOI and trial-registration fields are absent.
- No `trial_family_id` field exists.
- The retrieved valid-label data includes 619 rows labelled `significantly increase`, while the download documentation specifies `significantly increased`. These rows were excluded from the current prototype rather than silently normalized.

The official splits provide article-level separation, but they do not establish trial-family separation. Multiple prompts for one PMCID are expected and must remain grouped by article. The prototype does not freeze new train/calibration/test splits.

## MS² sample

The official repository sample contains one review, 20 included study groups/reports, PMIDs for all 20 reports, no DOI values, and no trial-registration identifiers. This is useful for schema inspection but cannot establish population-level trial-family coverage. The sample’s significance fields are not treated as gold cross-study effect directions.

## Prototype audit

- 64 clean instances and 64 omission instances.
- 64 unique prompt IDs.
- 6 unique article IDs in the bounded prototype because prompts are grouped by article.
- 0 trial-family IDs.
- 0 review IDs.
- No cross-split claims are made for this bounded artifact.

## Identity hierarchy

The feasible hierarchy is currently:

1. exact registration match — not available;
2. explicit dataset trial-family linkage — not available;
3. DOI/PMID identity — PMCID/PMID article identity only;
4. metadata linkage — not attempted, because heuristic merging could manufacture trial families;
5. unresolved — the default for underlying trial identity.

Conclusion: article-level leakage can be controlled using the provided EI splits, but trial-family leakage cannot currently be controlled from the inspected fields alone.
