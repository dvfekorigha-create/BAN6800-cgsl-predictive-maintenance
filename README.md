# CGSL Predictive Maintenance

BAN6800 Module 2 proof-of-concept repository for Chairborne Global Services Limited.

## Objective
Develop a human-supervised predictive and prescriptive analytics capability that identifies elevated equipment-failure risk, prioritizes maintenance/inspection, and supports operational availability.

## Repository structure
```text
cgsl-predictive-maintenance/
├── data/
│   ├── raw/
│   ├── processed/
│   └── data_dictionary/
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_preparation.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   ├── 04_model_development.ipynb
│   └── 05_evaluation_and_recommendations.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── evaluation.py
│   └── recommendations.py
├── models/
├── dashboards/
├── reports/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

## Dataset boundary
The UCI APS Failure at Scania Trucks dataset is used as a public proof-of-concept proxy. It is not CGSL proprietary data. Production deployment requires governed CGSL marine/offshore data and validation.

## Safety
Model outputs are decision support only. They do not override engineering, HSE, emergency, regulatory, or maintenance procedures.
