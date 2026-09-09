# BA-12 Risk Ranking Business Rules

Critical: risk score >= 0.50 -> Immediate technical review / inspection.

High: 0.10 <= risk score < 0.50 -> Prioritize technical review and planned inspection.

Lower: risk score < 0.10 -> Continue monitoring; no automatic intervention.

Risk rank is descending model score; rank 1 is highest.

UCI_TEST_##### identifiers are proxy observation IDs, not CGSL asset IDs.

Rules are initial demonstration rules and require production recalibration with governed CGSL data and actual costs.
