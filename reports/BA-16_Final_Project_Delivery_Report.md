# BA-16 Final Project Documentation and Handover

## Project
**AI-Enabled Predictive and Prescriptive Analytics for Marine Asset Maintenance and Operational Availability at CGSL**

### Purpose
BA-16 consolidates the completed Module 2 project evidence, final RAID position, key modelling decisions, dashboard outputs, governance controls, limitations, and production handover requirements.

## 1. Project delivery status

All planned workstreams BA-01 through BA-15 have been completed for the proof-of-concept scope. BA-16 is the final consolidation and handover workstream.

| Ticket | Workstream | Status | Key evidence |
|---|---|---|---|
| BA-01 | Repository / structure | Done | GitHub repository structure and README |
| BA-02 | Public proxy dataset | Done | `data/raw/` dataset files and provenance README |
| BA-03 | Data dictionary | Done | `data/data_dictionary/Preliminary_Data_Dictionary.xlsx` |
| BA-04 | Data understanding | Done | `notebooks/01_data_understanding.ipynb` and profiling outputs |
| BA-05 | Preprocessing | Done | `notebooks/02_data_preparation.ipynb` and processed arrays |
| BA-06 | Exploratory analysis | Done | `notebooks/03_exploratory_analysis.ipynb` and screening summary |
| BA-07 | Feature engineering | Done | `notebooks/04_feature_engineering.ipynb` and final feature mapping |
| BA-08 | Baseline classifier | Done | Logistic regression notebook, report and validation results |
| BA-09 | Classifier comparison | Done | 5-fold comparison of Logistic Regression, Random Forest and Gradient Boosting |
| BA-10 | Cost-sensitive threshold | Done | Threshold analysis and selected alert threshold |
| BA-11 | Model documentation | Done | Model card and evaluation report |
| BA-12 | Risk ranking | Done | Ranked observations, risk categories and business rules |
| BA-13 | Prescriptive rules | Done | Decision matrix and recommendation outputs |
| BA-14 | Power BI dashboard | Done | Three dashboard pages and supporting datasets |
| BA-15 | Privacy / fairness / explainability | Done | Governance document and monitoring/checklists |
| BA-16 | RAID / final documentation | In Progress | This final package and handover evidence |

## 2. Analytical outcome

The public UCI APS Failure at Scania Trucks dataset was used as a **proof-of-concept proxy**, not as CGSL proprietary data. The dataset contains 60,000 training observations, 16,000 test observations and 171 attributes.

Following preprocessing and feature engineering, 334 features were retained for modelling. The selected modelling path used Random Forest after stratified cross-validation comparison.

For cost-sensitive threshold selection, the internal evaluation used the documented UCI proxy costs of FP=10 and FN=500. The selected alert threshold was **0.10** rather than 0.50. On the internal evaluation split, this changed the results from precision 0.8280 / recall 0.6500 / F1 0.7283 / cost 35,270 at threshold 0.50 to precision 0.3621 / recall 0.9450 / F1 0.5235 / cost 8,830 at threshold 0.10, a 74.96% reduction in the proxy cost objective.

The official UCI test set was not used for model or threshold selection. It was subsequently used for the BA-12 risk-ranking demonstration after selection was complete; audit labels were retained for post-hoc verification only.

## 3. Decision-support layer

BA-12 and BA-13 convert model scores into operationally interpretable risk tiers and recommended actions:

- **Critical:** risk score >= 0.50 -> immediate technical review / inspection.
- **High:** 0.10 <= risk score < 0.50 -> prioritized technical review and planned inspection.
- **Lower:** risk score < 0.10 -> continue monitoring; no automatic intervention.

The design requires human oversight and does not enable autonomous operational control. Proxy observation identifiers are not CGSL asset identifiers.

## 4. Dashboard

The Power BI dashboard contains:

1. **Executive Risk Overview** – KPI cards, risk-category distribution, risk-score distribution and Top 10 highest-risk observations.
2. **Prescriptive Action Queue** – ranked action queue, risk and priority slicers, and priority distribution.
3. **Operational Decision Support** – risk overview, recommended actions and human review status.

## 5. Production handover requirements

Before a production deployment, the team must:

- replace the public proxy with governed CGSL vessel/equipment/maintenance/operational data;
- map real CGSL asset and equipment identifiers;
- validate label definitions and maintenance event windows;
- recalibrate thresholds using actual CGSL costs, safety criticality and operational consequences;
- implement approved privacy, access, retention, encryption and audit controls;
- conduct fairness monitoring on appropriate production-relevant subgroups where legally and operationally appropriate;
- validate model stability and drift monitoring;
- establish model/version approval and rollback procedures;
- obtain qualified technical/HSE review of recommendations;
- confirm enterprise access to required data, Azure and Power BI services.

## 6. Final limitation statement

This project demonstrates an end-to-end analytics workflow and decision-support prototype. It does **not** establish that the model is production-ready for CGSL marine assets, because the modelling evidence is based on a public truck-failure proxy dataset. Production claims require validation against governed CGSL data and real maintenance and operational outcomes.

## 7. Final evidence

See the BA-16 completion tracker workbook and evidence index for the exact repository location and expected evidence associated with each workstream.
