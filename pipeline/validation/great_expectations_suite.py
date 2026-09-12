from __future__ import annotations
from pathlib import Path
import json
import pandas as pd

SUITE_NAME = "cgsl_module3_data_quality_suite"


def build_expectation_suite() -> dict:
    return {
        "name": SUITE_NAME,
        "purpose": "Pre-transform validation contract for UCI APS Failure at Scania Trucks input.",
        "expectations": [
            {"expectation_type": "ExpectTableRowCountToBeBetween", "kwargs": {"min_value": 5000}},
            {"expectation_type": "ExpectTableColumnCountToEqual", "kwargs": {"value": 171}},
            {"expectation_type": "ExpectColumnValuesToNotBeNull", "kwargs": {"column": "class"}},
            {"expectation_type": "ExpectColumnValuesToBeInSet", "kwargs": {"column": "class", "value_set": ["neg", "pos"]}},
        ],
    }


def run_validation(df: pd.DataFrame, output_json: str = "evidence/gx_validation_results_deterministic.json") -> dict:
    results = [
        {"expectation": "ExpectTableRowCountToBeBetween", "success": bool(len(df) >= 5000), "observed": int(len(df))},
        {"expectation": "ExpectTableColumnCountToEqual", "success": bool(df.shape[1] == 171), "observed": int(df.shape[1])},
        {"expectation": "ExpectColumnValuesToNotBeNull", "success": bool(df["class"].notna().all()), "observed_nulls": int(df["class"].isna().sum())},
        {"expectation": "ExpectColumnValuesToBeInSet", "success": bool(set(df["class"].dropna().unique()).issubset({"neg", "pos"})), "observed": sorted(map(str, df["class"].dropna().unique()))},
    ]
    summary = {"suite_name": SUITE_NAME, "success": all(r["success"] for r in results), "results": results}
    Path(output_json).parent.mkdir(parents=True, exist_ok=True)
    Path(output_json).write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def save_suite_definition(path: str = "great_expectations/expectation_suite.json") -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(build_expectation_suite(), indent=2), encoding="utf-8")
