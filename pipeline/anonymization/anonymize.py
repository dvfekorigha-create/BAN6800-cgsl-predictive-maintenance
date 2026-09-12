from __future__ import annotations
import hashlib
import pandas as pd
from pipeline.logging.audit_log import AuditLogger


def anonymize_dataframe(df: pd.DataFrame, pii_columns: list[str] | None = None, identifier_columns: list[str] | None = None, audit: AuditLogger | None = None) -> pd.DataFrame:
    pii_columns = pii_columns or []
    identifier_columns = identifier_columns or []
    out = df.copy()
    removed = []
    hashed = []
    for col in pii_columns:
        if col in out.columns:
            out = out.drop(columns=[col])
            removed.append(col)
    for col in identifier_columns:
        if col in out.columns:
            out[col] = out[col].astype(str).map(lambda x: hashlib.sha256(x.encode()).hexdigest())
            hashed.append(col)
    if audit:
        audit.write("anonymization", removed_columns=removed, hashed_identifier_columns=hashed)
    return out
