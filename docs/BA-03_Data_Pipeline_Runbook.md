# BA-03 Data Pipeline Runbook

## Source
UCI APS Failure at Scania Trucks raw CSVs committed in `data/raw/`.

## Execution
1. Create a Python 3.12 environment.
2. `pip install -r requirements.txt`
3. Verify both raw files exist in `data/raw/`.
4. Run `python scripts/run_pipeline.py`.
5. Run `pytest -q tests`.
6. Optionally build/run the container with Docker.

## Pipeline gates
- Raw schema: 171 columns including `class`.
- Minimum rows: 5,000.
- Missing marker: `na`.
- Fail fast on critical schema/target validation failures.
- Drop features above 80% missingness using training data only.
- Learn medians on training data; reuse the same preprocessing artifact for test data.
- Add missingness indicators for retained features.
- Encode `neg`/`pos` as 0/1 in model-ready outputs.
- Run privacy/anonymization and representation-bias checks before output.
- Write data-access and transformation events to `logs/privacy_audit.jsonl`.
- Emit lineage and a pipeline run summary under `reports/` and `evidence/`.

## Reproducibility
Same source files + same configuration + same code version produce traceable training/test outputs. The preprocessing artifact records dropped columns, retained columns and training medians so test transformation does not refit on test data.
