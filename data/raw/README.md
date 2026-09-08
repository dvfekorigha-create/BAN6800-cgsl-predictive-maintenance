# UCI APS Failure at Scania Trucks Dataset

## Dataset Purpose

This project uses the UCI APS Failure at Scania Trucks dataset as a public proxy dataset for initial development and methodology validation of the CGSL Predictive Maintenance and Operational Availability project.

The dataset does not represent CGSL proprietary operational data. Production implementation would require governed CGSL vessel, equipment, maintenance, operational, and relevant contextual records.

## Source

UCI Machine Learning Repository

Dataset: APS Failure at Scania Trucks

Dataset ID: 421

DOI: 10.24432/C51S51

License: CC BY 4.0

## Dataset Characteristics

- Training dataset: 60,000 instances
- Test dataset: 16,000 instances
- Attributes: 171
- Target: failure/no-failure classification
- Missing values are represented as `na`
- The training data contains a highly imbalanced target distribution, with approximately 1,000 positive failure cases and 59,000 negative cases.

## Files

- `aps_failure_training_set.csv` — training dataset
- `aps_failure_test_set.csv` — test dataset
- `aps_failure_description.txt` — dataset description and source information

## Public Proxy Limitation

The UCI dataset is used only as a public proxy because CGSL proprietary operational data is not available for this academic project. Model findings and performance results must therefore not be interpreted as direct evidence of CGSL equipment failure patterns.

Any future production solution should be retrained and validated using appropriately governed CGSL operational data.

## Data Provenance

The dataset was obtained from the UCI Machine Learning Repository and is stored in this repository under `data/raw/` without modification to the original source files.
