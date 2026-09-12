# Data Lineage

**UCI raw CSV -> Prefect ingestion task -> schema and target validation -> duplicate detection -> missingness profile -> high-missingness feature removal -> numeric coercion -> median imputation -> missingness indicators -> target encoding -> privacy/anonymization check -> bias representation check -> model-ready CSV -> downstream Module 4 model development.**

Future production lineage will add CGSL source systems, ingestion timestamps, data-owner metadata, retention class, and warehouse/storage identifiers.
