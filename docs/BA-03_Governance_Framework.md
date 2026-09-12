# Data Governance Framework — Module 3

| Control | Policy | Implementation evidence |
|---|---|---|
| Access control | Least privilege; separate development/production access | Environment/config boundary; audit log |
| Data minimization | Collect only fields required for approved analytics use | Anonymization configuration |
| Retention | Define retention by approved data class and contract | Production policy gate |
| Integrity | Schema, completeness, type, duplicate and target checks before transformation | GX + pandas validation |
| Confidentiality | Encrypt data in transit/at rest in production | Deployment control; not applicable to public UCI proxy |
| Auditability | Log data access and transformations | JSONL privacy audit log |
| Change management | Version-control code, configs, suites and Dockerfile | GitHub repository |
| Human oversight | No automated operational control from model outputs | Module 2 governance boundary |

The current UCI dataset is a public proxy. CGSL production deployment requires an approved lawful purpose, access roles, retention schedule, data-owner sign-off, and technical controls before processing proprietary or personal data.
