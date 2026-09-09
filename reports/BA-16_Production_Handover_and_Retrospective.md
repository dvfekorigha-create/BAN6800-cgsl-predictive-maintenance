# BA-16 Production Handover and Retrospective

## What was delivered
A complete proof-of-concept workflow from data understanding through predictive modelling, cost-sensitive thresholding, risk ranking, prescriptive decision rules, Power BI reporting, and governance documentation.

## What worked well
- Data profiling and missingness were documented before modelling.
- Test data remained untouched for model and threshold selection.
- Model comparison was performed using stratified cross-validation.
- Threshold selection explicitly considered asymmetric error costs.
- Risk scores were converted into action-oriented business rules.
- Human oversight was retained throughout the decision-support design.
- Dashboard evidence was captured across executive, action-queue and operational decision-support views.

## Key lessons / decisions
1. Accuracy alone is unsuitable for the highly imbalanced failure-prediction problem; recall, precision, F1, ROC-AUC and cost are needed together.
2. Threshold choice materially changes the operational trade-off; the selected 0.10 threshold favors recall under the proxy cost structure.
3. Highly correlated features were not aggressively removed because many correlations involved missingness indicators and premature pruning could discard useful signal.
4. Public proxy data is sufficient for a workflow demonstration but not for CGSL production claims.
5. Recommendations must remain human-approved rather than being treated as autonomous control actions.

## Open production gates
- CGSL data access and data ownership approval.
- Production schema and label-definition approval.
- Actual cost / criticality calibration.
- Privacy, security and retention implementation.
- Fairness and explainability validation on production-relevant cohorts.
- Model drift monitoring and retraining governance.
- Technical and HSE approval of the decision matrix.
- Enterprise Power BI / Azure deployment readiness.

## Retrospective questions
### What should be retained?
The staged BA-01 to BA-16 workflow, evidence-based modelling gates, explicit proxy limitation, cost-sensitive evaluation and human-oversight requirement.

### What should be improved in the next iteration?
Use governed CGSL data, include vessel/equipment context, establish production-quality labels, test subgroup performance with sufficient sample sizes, and validate the recommendation rules with maintenance and HSE subject-matter experts.
