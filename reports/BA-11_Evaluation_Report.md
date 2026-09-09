# BA-11 Evaluation Report — CGSL Predictive Maintenance

## Executive Summary
The project evaluated a predictive-maintenance classification approach using the UCI APS Failure at Scania Trucks dataset as a public proxy for the CGSL use case.

The workflow progressed from a Logistic Regression baseline (BA-08), through five-fold classifier comparison (BA-09), to threshold and cost-sensitive evaluation of the Random Forest model (BA-10).

The evidence supports Random Forest as the strongest comparison-stage model and shows that a lower decision threshold can materially reduce weighted missed-failure cost under the UCI proxy cost assumptions.

## 1. Baseline Benchmark — BA-08
Logistic Regression was established as the baseline using the validated 334-feature representation.

Validation metrics:
- Precision: 0.3407
- Recall: 0.9300
- F1-score: 0.4987
- ROC-AUC: 0.9665

The baseline demonstrated strong recall but relatively low precision, illustrating the effect of class imbalance and the importance of evaluating more than accuracy.

## 2. Comparative Modelling — BA-09
Five-fold stratified cross-validation compared three models.

| Model | Mean Precision | Mean Recall | Mean F1 | Mean ROC-AUC |
|---|---:|---:|---:|---:|
| Random Forest | 0.8838 | 0.6550 | 0.7517 | 0.9863 |
| Logistic Regression | 0.3662 | 0.9100 | 0.5222 | 0.9649 |
| Gradient Boosting | 0.2441 | 0.9600 | 0.3892 | 0.9828 |

Random Forest achieved the strongest overall balance based on mean F1-score and also had the highest mean precision and ROC-AUC.

Gradient Boosting achieved the highest recall but generated substantially lower precision, while Logistic Regression provided high recall at a lower precision/F1 trade-off.

## 3. Threshold and Cost-Sensitive Evaluation — BA-10
Random Forest was carried forward for explicit threshold analysis.

The UCI APS challenge cost assumptions were applied:
- False positive = 10
- False negative = 500

The selected threshold was **0.10**.

Internal-evaluation comparison:

| Metric | Threshold 0.50 | Selected 0.10 |
|---|---:|---:|
| Precision | 0.8280 | 0.3621 |
| Recall | 0.6500 | 0.9450 |
| F1-score | 0.7283 | 0.5235 |
| Total cost | 35,270 | 8,830 |

The selected threshold reduced weighted cost by **74.96%** on the internal evaluation set.

The associated confusion-matrix change was:
- False positives: 27 → 333
- False negatives: 70 → 11

This demonstrates the operational trade-off clearly: the lower threshold creates more alerts but substantially reduces missed positive cases under the stated cost structure.

## 4. Overall Model Assessment
The model-development evidence supports the following conclusions:

1. Random Forest is the strongest comparison-stage classifier under the BA-09 cross-validation design.
2. Threshold selection materially changes the precision/recall balance.
3. Under the UCI cost assumptions, threshold 0.10 substantially lowers weighted cost compared with 0.50.
4. The correct production threshold for CGSL cannot be concluded from the proxy data alone because actual CGSL failure and inspection costs have not been established.
5. The model should therefore be treated as a human-supervised decision-support component rather than an autonomous maintenance controller.

## 5. Limitations
The UCI dataset is a public proxy derived from a truck-domain problem. It does not provide CGSL vessel identifiers, marine environmental variables, proprietary maintenance costs or other domain-specific operational context.

The anonymized feature names restrict physical interpretation of individual variables. Statistical associations are therefore not treated as mechanical causal explanations.

## 6. Governance Implications
Before production deployment, CGSL would need:
- Governed domain-specific data
- Approved target and event definitions
- Cost validation
- Data-quality controls
- Access and audit controls
- Model validation and approval
- Drift monitoring
- Explainability
- Human accountability
- Periodic threshold review

## 7. Recommended Next Step
BA-12 should translate the selected predictive output into a transparent risk-ranking framework. BA-13 should then define documented business rules that translate risk into prioritized actions for human review.

## Final Assessment
The project has established a reproducible modelling benchmark and a cost-sensitive decision-support approach. The evidence is sufficient for subsequent risk-ranking and prescriptive-rule development, while retaining the explicit boundary that the results are based on a public proxy dataset rather than CGSL proprietary operational data.
