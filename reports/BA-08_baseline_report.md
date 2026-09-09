# BA-08 Baseline Logistic Regression Report

## Purpose
Establish a reproducible baseline classifier for APS failure prediction using the prepared UCI APS feature representation.

## Data
- Training observations: 60,000
- Test observations: 16,000 (reserved for later evaluation)
- Final BA-07 features: 334
- Training target: 59,000 `neg` and 1,000 `pos`
- Positive-class prevalence: 1.67%

## Method
- Stratified 80/20 validation split from the training data.
- StandardScaler fitted within the training pipeline.
- Logistic Regression with `class_weight="balanced"`.
- Baseline classification threshold: 0.50.
- Random state: 42.
- No threshold tuning in BA-08.
- Official UCI test set was not used for baseline selection or tuning.

## Validation Results
- Precision: 0.3407
- Recall: 0.9300
- F1-score: 0.4987
- ROC-AUC: 0.9665

## Confusion Matrix
- True Negatives: 11440
- False Positives: 360
- False Negatives: 14
- True Positives: 186

## Interpretation
The baseline provides an initial benchmark for later model comparison. Because the dataset is highly imbalanced, recall, precision, F1-score and ROC-AUC are emphasized rather than accuracy alone.

The results are proxy-dataset validation results and should not be interpreted as direct evidence of CGSL vessel or equipment failure performance. The UCI feature names are anonymized, so physical sensor interpretations are not assigned.

## Intended Next Use
BA-09 will compare alternative classifiers using a consistent validation framework. BA-10 will examine threshold and cost-sensitive evaluation.
