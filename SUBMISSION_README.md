# BAN6800 Module 3 — Final Submission Package

Student: Disere Leghemo
Project: AI-Enabled Predictive and Prescriptive Analytics for Marine Asset Maintenance and Operational Availability

## Primary submission
- `BAN6800_Module_3_Data_Pipeline_Presentation_FINAL.pptx` — 11-slide technical presentation.
- `BAN6800_Module_3_AI_Disclosure_Form_FINAL.docx` — Module 3 AI disclosure.

## Technical evidence package
- `pipeline/` — Prefect ETL flow and processing functions.
- `great_expectations/` — expectation suite definition.
- `tests/` — pytest tests.
- `Dockerfile`, `.dockerignore`, `docker-compose.yml` — containerization.
- `docs/` — lineage, governance, anonymization, bias, runbook and implementation/communication plan.
- `configs/` — pipeline configuration.
- `scripts/` — execution helpers.
- `reports/` and `evidence/` — locations reserved for run evidence produced by the student against the GitHub repository's UCI raw data.

## Verification status
`pytest -q tests` was executed on the package and passed all available unit tests.

The actual end-to-end Prefect/Great Expectations/Docker run against the UCI raw CSVs must be executed in the student's environment before final submission. Do not claim those run results as passed until the generated evidence confirms success.

## Module 2 continuity
The Module 2 Data Dictionary identifies the UCI APS dataset as the public proof-of-concept proxy and documents future CGSL sources including asset/equipment IDs, maintenance history, operational measurements, and downtime/failure events. The Module 3 pipeline preserves that boundary.
