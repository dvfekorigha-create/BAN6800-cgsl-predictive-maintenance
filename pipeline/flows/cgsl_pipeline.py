from __future__ import annotations
from pathlib import Path
import pandas as pd
from prefect import flow, task
from pipeline.core.ingest import read_uci_csv
from pipeline.core.clean import fit_transform_train, transform_with_artifact
from pipeline.core.lineage import write_lineage
from pipeline.validation.great_expectations_suite import run_validation, save_suite_definition
from pipeline.validation.run_gx import run_gx
from pipeline.anonymization.anonymize import anonymize_dataframe
from pipeline.bias.detection import run_bias_detection
from pipeline.logging.audit_log import AuditLogger

@task(retries=2, retry_delay_seconds=5)
def ingest(path: str, audit_path: str = "logs/privacy_audit.jsonl") -> pd.DataFrame:
    audit = AuditLogger(audit_path)
    audit.write("data_access", source=path, action="read_raw_csv")
    return read_uci_csv(path)

@task
def validate_raw(df: pd.DataFrame, audit_path: str = "logs/privacy_audit.jsonl"):
    audit = AuditLogger(audit_path)
    deterministic = run_validation(df)
    gx = run_gx(df)
    audit.write("data_validation", rows=len(df), columns=len(df.columns), deterministic_success=deterministic["success"], gx_success=gx.get("success"))
    if not deterministic["success"]:
        raise ValueError(f"Raw data validation failed: {deterministic}")
    return {"deterministic": deterministic, "gx": gx}

@task
def process_train(df: pd.DataFrame, artifact_path: str = "data/processed/preprocessing_artifact.json", audit_path: str = "logs/privacy_audit.jsonl"):
    transformed, artifact, stats = fit_transform_train(df)
    artifact.save(artifact_path)
    AuditLogger(audit_path).write("pipeline_transform", stage="training_preparation", **stats)
    return transformed, artifact, stats

@task
def process_test(df: pd.DataFrame, artifact, audit_path: str = "logs/privacy_audit.jsonl"):
    transformed, stats = transform_with_artifact(df, artifact)
    AuditLogger(audit_path).write("pipeline_transform", stage="test_preparation", **stats)
    return transformed, stats

@task
def privacy_and_bias(df: pd.DataFrame, audit_path: str = "logs/privacy_audit.jsonl"):
    audit = AuditLogger(audit_path)
    out = anonymize_dataframe(df, pii_columns=[], identifier_columns=[], audit=audit)
    bias = run_bias_detection(out)
    audit.write("bias_assessment", status=bias["protected_group_fairness_status"], target_positive_share=bias["positive_class_share"])
    return out, bias

@flow(name="cgsl-module3-data-pipeline", log_prints=True)
def cgsl_pipeline(
    training_path: str = "data/raw/aps_failure_training_set.csv",
    test_path: str = "data/raw/aps_failure_test_set.csv",
    train_output: str = "data/processed/module3_model_ready_training.csv",
    test_output: str = "data/processed/module3_model_ready_test.csv",
):
    Path("evidence").mkdir(exist_ok=True)
    Path("logs").mkdir(exist_ok=True)
    save_suite_definition()

    train_raw = ingest(training_path)
    test_raw = ingest(test_path)
    train_validation = validate_raw(train_raw)
    test_validation = validate_raw(test_raw)
    train_private, train_bias = privacy_and_bias(train_raw)
    test_private, _ = privacy_and_bias(test_raw)
    train_processed, artifact, train_stats = process_train(train_private)
    test_processed, test_stats = process_test(test_private, artifact)

    Path(train_output).parent.mkdir(parents=True, exist_ok=True)
    train_processed.to_csv(train_output, index=False)
    test_processed.to_csv(test_output, index=False)
    AuditLogger().write("pipeline_output", training_output=train_output, test_output=test_output)
    write_lineage()

    summary = {
        "training_output": train_output,
        "test_output": test_output,
        "training_validation": train_validation,
        "test_validation": test_validation,
        "training_processing": train_stats,
        "test_processing": test_stats,
        "bias_status": train_bias["protected_group_fairness_status"],
    }
    Path("evidence/pipeline_run_summary.json").write_text(pd.Series(summary, dtype=object).to_json(indent=2), encoding="utf-8")
    print(summary)
    return summary

if __name__ == "__main__":
    cgsl_pipeline()
