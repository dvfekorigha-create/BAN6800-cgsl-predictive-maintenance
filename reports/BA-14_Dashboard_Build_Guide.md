# BA-14 Power BI Dashboard Build Guide

## Purpose
Build a management decision-support dashboard for the CGSL predictive-maintenance project using the BA-12 risk ranking and BA-13 prescriptive recommendations.

## Data source
Import `BA-14_dashboard_ready_risk_dataset.csv` into Power BI Desktop and rename the table to `RiskData`.

The dashboard is based on proxy UCI test observations. `Observation_ID` values such as `UCI_TEST_#####` are proxy IDs, not CGSL asset IDs.

## Recommended dashboard pages

### Page 1 — Executive Risk Overview
KPI cards:
- Total Observations
- Critical Count
- High Count
- High Plus Critical %
- Average Risk Score
- Maximum Risk Score

Visuals:
1. Donut or stacked column: Risk_Category by Observation Count.
2. Column chart: Priority_Level (P1/P2/P3) by count.
3. Histogram/column chart: Risk_Score distribution.
4. Table: Top 10 highest-risk observations with Risk_Rank, Observation_ID, Risk_Score, Risk_Category, Priority_Level, Recommended_Action.

### Page 2 — Prescriptive Action Queue
Use a table/matrix with:
- Risk_Rank
- Observation_ID
- Risk_Score
- Risk_Category
- Priority_Level
- Recommended_Action
- Review_Status
- Decision_Owner
- Human_Approval_Required

Add slicers for Risk_Category, Priority_Level, Review_Status, and Decision_Owner.

### Page 3 — Operational Decision Support
Use cards/charts for:
- Critical and High counts
- Recommended actions by category
- Evidence_To_Check
- Operational_Response
- Planning_Response

Add a clear note: recommendations require human validation and approval; autonomous control is not enabled.

## Formatting
- Format `Risk_Score` as percentage with 1 decimal place.
- Sort Risk_Category using `Risk_Band_Order`.
- Sort Priority_Level using `Priority_Order`.
- Sort the Top Risk table by Risk_Rank ascending.
- Use conditional formatting on Risk_Score and Priority_Level.

## Required business notes
Display these on the dashboard:
- Critical: risk score >= 0.50 → immediate technical review / inspection.
- High: 0.10 <= risk score < 0.50 → prioritize technical review and planned inspection.
- Lower: risk score < 0.10 → continue monitoring; no automatic intervention.
- Human approval is required; autonomous control is not enabled.
- These are demonstration rules and require recalibration using governed CGSL data and actual costs before production.
