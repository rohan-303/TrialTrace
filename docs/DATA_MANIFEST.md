# Milestone 1 source and artifact manifest

## Acquired artifacts

The prototype acquired:

- MS² official `sample.json` and README for schema inspection.
- Evidence Inference 2.0 `v2.0.tar.gz` from the official download endpoint.
- Extracted EI annotation/prompt CSVs and split files for bounded local inspection.

Raw archives and extracted clinical text are excluded from Git by repository rules. The compact manifest records byte sizes and SHA-256 hashes.

## Authoritative sources

- MS² repository: https://github.com/allenai/ms2
- MS² sample: https://raw.githubusercontent.com/allenai/ms2/master/sample.json
- MSLR2022 shared task: https://github.com/allenai/mslr-shared-task
- MSLR2022 direct archive: https://ai2-s2-mslr.s3.us-west-2.amazonaws.com/mslr_data.tar.gz
- Evidence Inference download page: https://evidence-inference.ebm-nlp.com/download/
- Evidence Inference 2.0 archive: https://evidence-inference.ebm-nlp.com/v2.0.tar.gz
- Evidence Inference code/license: https://github.com/jayded/evidence-inference

## Licensing and redistribution

The MS² repository contains Apache-2.0 code/repository material, while its README states that the dataset is licensed under the Semantic Scholar API and Dataset License Agreement. The MSLR2022 README reports an approximately 253 MB archive and points to Hugging Face/direct S3 access. Dataset redistribution terms must be reviewed separately from repository-code licensing.

Evidence Inference’s GitHub repository code is MIT-licensed. The public v2.0 data download exposes article text and annotations; this milestone records the endpoint and source terms but does not treat the code license as proof that all underlying article text is freely redistributable. Future release packaging should distribute manifests, transformations, and source identifiers unless article-level rights are verified.

## Manifest location

`data/manifests/milestone_1_source_manifest.json` contains the retrieved file paths, byte sizes, SHA-256 hashes, source URLs, and license references. `data/manifests/milestone_1_audit.json` contains the measured schema and prototype counts.
