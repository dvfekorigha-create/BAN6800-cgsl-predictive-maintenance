# Module 3 Evidence Status

| Evidence | Artifact | Status | Note |
|---|---|---|---|
| Pipeline code | `pipeline/` | Ready | Executable Prefect flow |
| Great Expectations | `great_expectations/`, `pipeline/validation/` | Ready | Suite + runner |
| Pytest | `tests/` | Ready | Core transformation/anonymization/validation tests |
| Docker | `Dockerfile` | Ready | Python 3.12 container |
| Bias | `pipeline/bias/`, `docs/BA-03_Bias_Detection_Plan.md` | Ready | Proxy representation check + future Fairlearn path |
| Anonymization | `pipeline/anonymization/` | Ready | PII removal + identifier hashing |
| Privacy audit | `pipeline/logging/` | Ready | JSONL event log |
| Lineage | `docs/BA-03_Data_Lineage.md` | Ready | Raw-to-model-ready flow |
| Real UCI pipeline run evidence | `evidence/` | **Run required by student** | Capture Prefect/GX/pytest/Docker outputs against repository raw UCI files before final submission |
