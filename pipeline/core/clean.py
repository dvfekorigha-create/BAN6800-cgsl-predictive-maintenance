from __future__ import annotations
from dataclasses import dataclass
import json
from pathlib import Path
import pandas as pd

@dataclass
class PreprocessorArtifact:
    dropped_columns: list[str]
    medians: dict[str, float]
    retained_columns: list[str]

    def save(self, path: str) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_text(json.dumps(self.__dict__, indent=2, allow_nan=False), encoding="utf-8")


def _feature_frame(df: pd.DataFrame) -> pd.DataFrame:
    if "class" not in df.columns:
        raise ValueError("Expected target column 'class'.")
    return df.drop(columns=["class"]).apply(pd.to_numeric, errors="coerce")


def fit_transform_train(df: pd.DataFrame, missing_threshold: float = 0.80) -> tuple[pd.DataFrame, PreprocessorArtifact, dict]:
    work = df.copy()
    duplicates_removed = int(work.duplicated().sum())
    work = work.drop_duplicates().reset_index(drop=True)
    target = work["class"].copy()
    features = _feature_frame(work)
    missing_rate = features.isna().mean()
    dropped_cols = missing_rate[missing_rate > missing_threshold].index.tolist()
    features = features.drop(columns=dropped_cols)
    medians = features.median(numeric_only=True).fillna(0.0)
    imputed = features.fillna(medians)
    indicators = features.isna().astype("int8")
    indicators.columns = [f"{c}__missing" for c in indicators.columns]
    transformed = pd.concat([imputed, indicators], axis=1)
    transformed["class"] = target.map({"neg": 0, "pos": 1}).astype("int8")
    artifact = PreprocessorArtifact(dropped_columns=dropped_cols, medians={k: float(v) for k,v in medians.items()}, retained_columns=list(features.columns))
    stats = {
        "input_rows": int(len(df)),
        "output_rows": int(len(work)),
        "duplicates_removed": duplicates_removed,
        "input_feature_count": int(df.shape[1] - 1),
        "dropped_high_missing_features": dropped_cols,
        "output_feature_count_including_missing_flags": int(transformed.shape[1] - 1),
        "remaining_missing_cells": int(transformed.drop(columns=["class"]).isna().sum().sum()),
    }
    return transformed, artifact, stats


def transform_with_artifact(df: pd.DataFrame, artifact: PreprocessorArtifact) -> tuple[pd.DataFrame, dict]:
    work = df.copy()
    duplicates_removed = int(work.duplicated().sum())
    work = work.drop_duplicates().reset_index(drop=True)
    target = work["class"].copy() if "class" in work.columns else None
    features = _feature_frame(work) if target is not None else work.apply(pd.to_numeric, errors="coerce")
    missing_before = features[artifact.retained_columns].isna()
    features = features.drop(columns=[c for c in artifact.dropped_columns if c in features.columns], errors="ignore")
    features = features.reindex(columns=artifact.retained_columns)
    medians = pd.Series(artifact.medians)
    imputed = features.fillna(medians)
    indicators = missing_before.astype("int8")
    indicators.columns = [f"{c}__missing" for c in indicators.columns]
    transformed = pd.concat([imputed, indicators], axis=1)
    if target is not None:
        transformed["class"] = target.map({"neg": 0, "pos": 1}).astype("int8")
    stats = {"input_rows": int(len(df)), "output_rows": int(len(work)), "duplicates_removed": duplicates_removed, "remaining_missing_cells": int(transformed.isna().sum().sum())}
    return transformed, stats


def clean_and_transform(df: pd.DataFrame, missing_threshold: float = 0.80) -> tuple[pd.DataFrame, list[str], dict]:
    transformed, artifact, stats = fit_transform_train(df, missing_threshold)
    return transformed, artifact.dropped_columns, stats
