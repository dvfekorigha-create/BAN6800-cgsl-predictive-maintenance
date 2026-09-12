from __future__ import annotations
from pathlib import Path

def write_lineage(path: str = "reports/data_lineage.md") -> None:
    Path(path).write_text("""# Data Lineage — BAN6800 Module 3

**Source:** UCI APS Failure at Scania Trucks raw training/test CSVs.

**Flow:** raw CSV -> ingestion (20 metadata rows skipped; `na` interpreted as missing) -> duplicate detection -> missingness profiling -> remove features above 80% missing -> numeric coercion -> median imputation -> missingness indicators -> class encoding (`neg=0`, `pos=1`) -> validated processed output.

**Future CGSL extension:** governed vessel/equipment identifiers, maintenance history, operational measurements, and downtime/failure events will replace/augment the public proxy after data-access and governance approval.

**Privacy boundary:** current UCI proxy contains anonymized feature names and no identified CGSL personnel data. Production implementation must apply access control, retention, minimization, and audit logging to CGSL data.
""", encoding="utf-8")
