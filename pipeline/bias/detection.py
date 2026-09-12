from __future__ import annotations
import json
from pathlib import Path
import pandas as pd


def run_bias_detection(df: pd.DataFrame, y_true_col: str = "class", y_pred_col: str | None = None, sensitive_columns: list[str] | None = None, output: str = "evidence/bias_report.json") -> dict:
    sensitive_columns = sensitive_columns or []
    total = len(df)
    counts = df[y_true_col].value_counts(dropna=False)
    report = {
        "assessment_scope": "Representation bias plus protected-group fairness readiness",
        "target_representation": {str(k): {"count": int(v), "share": round(float(v / total), 6)} for k, v in counts.items()},
        "positive_class_share": float((df[y_true_col] == "pos").mean()),
        "protected_group_fairness_status": "not_assessable" if not sensitive_columns else "pending_metric_run",
        "minimum_group_support_rule": 30,
        "sensitive_group_assessment": [],
    }

    if sensitive_columns and y_pred_col and y_pred_col in df.columns:
        try:
            from fairlearn.metrics import MetricFrame, selection_rate, true_positive_rate, false_positive_rate
            y_true = (df[y_true_col] == "pos").astype(int)
            y_pred = df[y_pred_col].astype(int)
            for col in sensitive_columns:
                if col not in df.columns:
                    report["sensitive_group_assessment"].append({"column": col, "status": "not_available"})
                    continue
                mf = MetricFrame(
                    metrics={"selection_rate": selection_rate, "TPR": true_positive_rate, "FPR": false_positive_rate},
                    y_true=y_true,
                    y_pred=y_pred,
                    sensitive_features=df[col],
                )
                report["sensitive_group_assessment"].append({"column": col, "status": "assessed", "by_group": mf.by_group.to_dict()})
        except Exception as exc:
            report["fairlearn_error"] = repr(exc)
    elif sensitive_columns:
        report["fairness_note"] = "Sensitive groups were configured, but predictions were not supplied; metric execution is deferred to the modelling stage."

    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(output).write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    return report
