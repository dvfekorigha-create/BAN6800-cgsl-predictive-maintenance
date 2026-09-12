from __future__ import annotations
from pathlib import Path
import pandas as pd


def read_uci_csv(path: str | Path, skiprows: int = 20) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {p}")
    df = pd.read_csv(p, skiprows=skiprows, na_values=["na"], low_memory=False)
    if "class" not in df.columns:
        raise ValueError(f"Expected target column 'class' in {p}")
    return df
