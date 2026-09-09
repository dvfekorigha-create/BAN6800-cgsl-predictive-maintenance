# BA-13 Prescriptive Business Rules

## Purpose
Translate the BA-12 Random Forest risk score into actionable, human-supervised maintenance and operational recommendations.

## Decision principle
The model is a decision-support tool. A risk score does not automatically trigger a shutdown, maintenance execution, or other autonomous control. Every recommendation requires human validation against current operating conditions, alarms, maintenance history, defects, safety requirements, and approved maintenance processes.

## Prescriptive tiers
| Risk | Priority | Rule | Recommended response |
|---|---|---|---|
| Critical | P1 | score >= 0.50 | Immediate technical review / inspection; escalate to responsible maintenance/operations lead; create/prioritize work item after human validation. |
| High | P2 | 0.10 <= score < 0.50 | Prioritize technical review and planned inspection; assess whether maintenance should be brought forward. |
| Lower | P3 | score < 0.10 | Continue monitoring; maintain routine inspection/maintenance cadence; no automatic intervention. |

## Human approval gate
1. Review the model score and risk category.
2. Verify current condition evidence and operational context.
3. Confirm the recommended action is appropriate and safe.
4. Approve, modify, or reject the recommendation.
5. Record the decision and supporting rationale.

## Governance constraints
- No autonomous shutdown or control action.
- No automatic maintenance execution.
- Rules are initial demonstration rules and must be recalibrated with governed CGSL data, actual failure costs, operational constraints, and approved procedures before production use.
- `UCI_TEST_#####` values are proxy observation IDs, not CGSL asset IDs.

## BA-13 output
The accompanying recommendation dataset adds operational response, planning response, evidence-to-check, rationale, decision owner, and human-approval fields to the BA-12 risk-ranked data.
