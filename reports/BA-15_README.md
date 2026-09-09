# BA-15 README

## Deliverable
Privacy, Fairness & Explainability governance package for the CGSL predictive-maintenance project.

## Files
- `BA-15_PRIVACY_FAIRNESS_EXPLAINABILITY.md` — main governance narrative.
- `BA-15_privacy_controls_checklist.csv` — privacy, fairness, explainability, human-oversight and audit controls.
- `BA-15_fairness_monitoring_plan.csv` — production subgroup monitoring plan.
- `BA-15_explainability_plan.csv` — alert-level and model-level explanation plan.
- `BA-15_governance_config.json` — machine-readable governance settings.

## Key design position
The current UCI dataset is a public proxy. It does not establish production fairness or privacy compliance for CGSL. Production deployment requires governed CGSL data, formal privacy/security review, subgroup monitoring, model validation, recalibration using actual business costs, and authorised human approval.
