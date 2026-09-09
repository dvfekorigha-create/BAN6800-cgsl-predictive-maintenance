# BA-11 Model Card — CGSL Predictive Maintenance

## Model
**Selected model:** Random Forest classifier  
**Project:** AI-Enabled Predictive and Prescriptive Analytics for Marine Asset Maintenance and Operational Availability at CGSL  
**Dataset:** UCI APS Failure at Scania Trucks (public proxy)

## Intended Use
The model is intended as a proof-of-concept decision-support component for identifying elevated equipment-failure risk and supporting prioritization of maintenance or inspection.

It is **not** intended to autonomously control equipment, authorize maintenance, or make safety-critical decisions without human review.

## Data and Project Boundary
The project uses the UCI APS Failure at Scania Trucks dataset as a public proxy. The training data contain 60,000 observations and 171 original attributes. After BA-05 preprocessing and BA-07 feature validation, the modelling representation contains 334 features.

The UCI dataset is not CGSL proprietary operational data. Its truck-domain context limits direct transfer to CGSL marine/offshore assets. Any production implementation would require governed CGSL vessel, equipment, maintenance, operational and contextual data, followed by domain-specific validation.

## Preprocessing
The modelling representation was produced through the documented BA-05/BA-07 workflow:
- Two features with more than 80% missingness were removed: `bq_000` and `br_000`.
- Remaining numeric features were median-imputed.
- Missingness indicators were retained.
- The imputer was fitted on training data only.
- One zero-variance feature, `cd_000`, was removed in BA-07.
- No aggressive correlation pruning was performed; the final 334-feature representation was retained for modelling.

## Model Selection Evidence

### BA-08 Baseline
Logistic Regression with `class_weight="balanced"` was used as the baseline.

Validation results:
- Precision: 0.3407
- Recall: 0.9300
- F1-score: 0.4987
- ROC-AUC: 0.9665

### BA-09 Cross-Validation Comparison
Five-fold stratified cross-validation compared Logistic Regression, Random Forest and Gradient Boosting.

| Model | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|
| Random Forest | 0.8838 | 0.6550 | 0.7517 | 0.9863 |
| Logistic Regression | 0.3662 | 0.9100 | 0.5222 | 0.9649 |
| Gradient Boosting | 0.2441 | 0.9600 | 0.3892 | 0.9828 |

Random Forest was the provisional comparison-stage leader because it achieved the strongest mean F1-score, precision and ROC-AUC.

## Threshold and Cost-Sensitive Evaluation
BA-10 evaluated the Random Forest threshold using the UCI proxy cost structure:
- False positive cost = 10
- False negative cost = 500

A threshold of **0.10** minimized the weighted cost on the threshold-tuning partition.

On the separate internal-evaluation partition:
- Threshold 0.50 total cost: 35,270
- Threshold 0.10 total cost: 8,830
- Cost reduction: 26,440 (74.96%)
- Recall: 0.9450 at threshold 0.10
- Precision: 0.3621 at threshold 0.10
- F1-score: 0.5235 at threshold 0.10
- ROC-AUC: 0.9811

The lower threshold substantially reduces false negatives at the expense of more false positives.

**Important:** the threshold is cost-optimal under the UCI proxy assumptions only. Actual CGSL costs should be obtained and validated before production use.

## Validation and Leakage Controls
- BA-09 used five-fold StratifiedKFold cross-validation.
- The official UCI test set was not used for model comparison or threshold selection.
- BA-10 used separate model-fit, threshold-tuning and internal-evaluation partitions.
- Threshold tuning was performed only on the tuning partition.
- The selected threshold was evaluated on a separate internal holdout.
- Preprocessing was designed to avoid leakage by fitting training-derived transformations only on training data.

## Performance Interpretation
The modelling results show a clear precision/recall trade-off. Random Forest offered the strongest overall balance at the default comparison threshold, while the cost-sensitive threshold increased recall substantially and reduced weighted cost under the UCI assumptions.

These results should be interpreted as methodological evidence on a public proxy dataset, not as measured CGSL operational performance.

## Known Limitations and Risks
1. **Domain mismatch:** the public data describe heavy trucks, not CGSL marine/offshore assets.
2. **Anonymized features:** physical meanings of individual UCI variables are not available for reliable mechanical interpretation.
3. **Class imbalance:** positive cases are a small minority, so accuracy alone is unsuitable as the primary metric.
4. **Cost transfer risk:** UCI's 10/500 cost assumptions are not established CGSL maintenance costs.
5. **Model drift:** production performance could change as equipment, operating conditions, maintenance practices or data collection change.
6. **Automation bias:** model outputs must remain advisory and subject to qualified human review.
7. **Data quality:** production deployment would require controlled data definitions, quality checks, access controls and monitoring.

## Explainability and Governance
The model should be used with documented risk scores, validation results and appropriate explanation methods. Production governance should include model versioning, audit logging, access control, drift monitoring, validation before release and clear human accountability.

## Fairness and Privacy
The current UCI proxy contains anonymized operational variables and is not a sufficient basis for claims about personnel fairness or CGSL demographic impacts. Any future CGSL implementation involving personal data should apply data minimization, purpose limitation, access control, retention controls and applicable Nigerian data-protection requirements.

## Recommended Monitoring
For a future production implementation, monitor:
- Precision, recall and F1
- False-negative rate
- Cost-sensitive performance
- Data-quality and missingness drift
- Feature distribution drift
- Alert volume and false-alarm burden
- Model/version changes
- Human review and override patterns

## Model Status
**Status:** Proof-of-concept / academic project benchmark  
**Production approval:** Not established

## Reproducibility
Supporting evidence is versioned in the GitHub project through the BA-08, BA-09 and BA-10 notebooks, reports and model artifacts.
