# BAN6800 Module 3 — Student Run & Evidence Checklist

## A. Repository setup
1. Keep the UCI raw files in `data/raw/`:
   - `aps_failure_training_set.csv`
   - `aps_failure_test_set.csv`
   - `aps_failure_description.txt`
2. Add the Module 3 pipeline folders/files to the existing GitHub repository.

## B. Local/Colab execution
```bash
pip install -r requirements.txt
python scripts/run_pipeline.py
pytest -q tests
```

Optional Docker verification:
```bash
docker build -t cgsl-module3 .
docker run --rm -v "$PWD/data:/app/data" -v "$PWD/reports:/app/reports" -v "$PWD/evidence:/app/evidence" -v "$PWD/logs:/app/logs" cgsl-module3
```

## C. Evidence that must be captured
- Prefect flow completes successfully for training and test inputs.
- `evidence/gx_validation_results.json` shows the Great Expectations suite passing.
- `pytest -q tests` shows all tests passed.
- Docker build and run complete without error.
- `evidence/bias_report.json` records target representation and protected-group fairness assessability.
- `logs/privacy_audit.jsonl` contains data-access, validation, anonymization, bias and output events.
- `data/processed/module3_model_ready_training.csv` and `module3_model_ready_test.csv` exist.
- `data/processed/preprocessing_artifact.json` exists and documents the training-fitted preprocessing parameters.
- `reports/data_lineage.md` exists.

## D. Presentation evidence
Replace any pending-evidence wording with the student's actual execution screenshots after the first complete run. Do not claim a pipeline run has passed until the command output and evidence files confirm it.
