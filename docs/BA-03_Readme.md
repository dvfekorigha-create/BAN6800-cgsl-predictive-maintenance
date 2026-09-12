# BAN6800 Module 3 — Reproducible Data Pipeline

This package implements the Module 3 data-engineering layer for the CGSL predictive-maintenance capstone.

**Public proxy:** UCI APS Failure at Scania Trucks.

**Pipeline scope:** ingestion, validation, training-fitted preprocessing, test transformation, privacy/anonymization checks, representation-bias assessment, audit logging, lineage, tests and containerization.

**Important boundary:** the UCI proxy is not CGSL proprietary data. Production deployment requires governed CGSL vessel/equipment/maintenance/operational data and approved access controls.

**Required final evidence:** actual Prefect flow run, Great Expectations validation result, pytest output, Docker build/run evidence, bias report, privacy audit log, processed training/test outputs and lineage artifact.
