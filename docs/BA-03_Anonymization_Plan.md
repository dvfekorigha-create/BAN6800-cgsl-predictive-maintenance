# Data Anonymization Plan

1. Detect candidate PII/identifier columns from the source schema and approved data dictionary.
2. Remove direct identifiers unless essential to the workflow.
3. Hash approved operational identifiers when linking is required; keep the mapping key outside analytics storage.
4. Never expose personal names, emails, phone numbers, or government identifiers in dashboards or model features without explicit governance approval.
5. Log removals/hash operations in the privacy audit log.
6. For the current UCI proxy, feature names are anonymized and no CGSL personnel identifiers are expected; the pipeline therefore performs a no-op anonymization pass and records that result.
