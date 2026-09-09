# BA-15 Privacy, Fairness & Explainability

## Project
AI-Enabled Predictive and Prescriptive Analytics for Marine Asset Maintenance and Operational Availability at CGSL

## Purpose
This governance package defines the minimum privacy, fairness, explainability, and human-oversight controls for the predictive-maintenance decision-support solution.

## 1. Scope and data boundary
The current analytical work uses the UCI APS Failure at Scania Trucks dataset as a public proxy. It is not CGSL proprietary asset or personnel data. Production deployment must replace or augment the proxy with governed CGSL vessel/equipment, maintenance, operational, and relevant contextual records.

The current BA-12 risk-ranking output uses proxy observation identifiers (`UCI_TEST_#####`). These identifiers must not be presented as CGSL asset identifiers.

## 2. Privacy and data protection controls
### Pre-production controls
- Establish a documented production data inventory and data lineage for each source.
- Identify whether each field is operational, personal, sensitive, or non-personal before ingestion.
- Apply data minimisation: collect only data needed for maintenance-risk prediction and operational decision support.
- Define retention periods and secure disposal rules for raw, processed, feature-store, prediction, and audit data.
- Enforce role-based access control using least privilege.
- Protect data in transit and at rest using organisation-approved security controls.
- Keep model outputs and audit records access-controlled because they may influence operational decisions.
- Maintain access/audit logs for sensitive production datasets and decision records.
- Complete a formal privacy/legal review before production use and align controls with applicable Nigerian data-protection requirements and CGSL policy.

### Privacy-by-design principle
No personal data should be introduced into the predictive pipeline solely because it is available. Any production field must have a documented business purpose, lawful basis/authorisation as applicable, access rule, retention rule, and owner.

## 3. Fairness and subgroup monitoring
The current public proxy contains anonymised technical features and does not provide the protected-group context required for a full fairness assessment. Therefore, no claim of demonstrated fairness is made from the current proxy analysis.

For governed CGSL production data, define relevant operational subgroups only where they are legitimate for monitoring and decision quality. Examples may include vessel class, equipment family, asset age band, operating environment, duty cycle, or maintenance regime. Do not create sensitive-group analyses unless the data is lawfully collected and the review has a justified purpose.

Required monitoring measures:
- false-negative rate by relevant subgroup;
- recall by relevant subgroup;
- precision by relevant subgroup;
- alert rate by subgroup;
- calibration/risk-score distribution by subgroup where feasible.

Investigate material disparities. Any mitigation must be documented, validated, and approved before deployment.

## 4. Explainability approach
The solution is intended to support maintenance and operations personnel, not replace their judgement.

### Minimum explanation for each alert
- risk score;
- risk category;
- priority level;
- recommended action;
- decision owner / reviewer;
- evidence or operational checks to verify before action.

### Model-level explanation
For the Random Forest model, use feature-importance and local explanation methods where available in the implementation environment. Explanations should be treated as decision-support evidence rather than proof of causality.

### User-facing language
Avoid statements such as “the equipment will fail.” Prefer wording such as “the model estimates elevated failure risk based on the observed input pattern; technical review is required.”

## 5. Human oversight
Human oversight is mandatory. The BA-12 rules specify human oversight and no autonomous control. Critical alerts require immediate technical review/inspection; High alerts require prioritised technical review/planned inspection; Lower-risk observations remain under monitoring.

No model output should directly trigger autonomous shutdown, dispatch, maintenance work order creation, or other irreversible operational action without authorised human review and approval.

## 6. Auditability and governance evidence
Retain:
- model version and configuration;
- training data provenance;
- preprocessing and feature mapping version;
- threshold and cost assumptions;
- prediction timestamp;
- risk score/category/priority;
- recommendation shown to the reviewer;
- reviewer/decision owner;
- final human decision and reason, where captured;
- material overrides and exceptions;
- monitoring results and model-review outcomes.

## 7. Known limitations
1. The current dataset is a public proxy, not CGSL production data.
2. The anonymised proxy does not support a complete production fairness assessment.
3. BA-12 risk rules are demonstration rules and require recalibration with governed CGSL data and actual costs.
4. Explanations indicate model drivers/patterns and must not be interpreted as causal engineering findings.
5. Production use requires formal data governance, security, privacy, operational validation, and approval.

## 8. Acceptance criteria for BA-15
BA-15 can be considered complete when:
- privacy/data-boundary controls are documented;
- production data owners and access controls are defined;
- subgroup fairness monitoring is specified and its current proxy limitation is recorded;
- model and alert explainability requirements are documented;
- human approval is explicit;
- audit evidence requirements are defined;
- production limitations and recalibration requirements are stated.
