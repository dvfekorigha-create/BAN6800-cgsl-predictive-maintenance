from __future__ import annotations
import json
from pathlib import Path
import pandas as pd

SUITE_NAME = "cgsl_module3_data_quality_suite"


def run_gx(df: pd.DataFrame, output_json: str = "evidence/gx_validation_results.json") -> dict:
    """Build and execute a Great Expectations Core ExpectationSuite against a pandas batch."""
    Path(output_json).parent.mkdir(parents=True, exist_ok=True)
    try:
        import great_expectations as gx

        context = gx.get_context()
        data_source = context.data_sources.add_pandas(name="cgsl_module3_runtime_source")
        asset = data_source.add_dataframe_asset(name="runtime_dataframe")
        batch_definition = asset.add_batch_definition_whole_dataframe("whole_dataframe")

        suite = gx.ExpectationSuite(name=SUITE_NAME)
        expectations = [
            gx.expectations.ExpectTableRowCountToBeBetween(min_value=5000),
            gx.expectations.ExpectTableColumnCountToEqual(value=171),
            gx.expectations.ExpectColumnValuesToNotBeNull(column="class"),
            gx.expectations.ExpectColumnValuesToBeInSet(column="class", value_set=["neg", "pos"]),
        ]
        for expectation in expectations:
            suite.add_expectation(expectation)

        Path("great_expectations").mkdir(exist_ok=True)
        Path("great_expectations/expectation_suite_runtime.json").write_text(
            json.dumps(suite.to_json_dict(), indent=2, default=str), encoding="utf-8"
        )

        validation_definition = gx.ValidationDefinition(
            data=batch_definition, suite=suite, name="cgsl_module3_validation"
        )
        validation_definition = context.validation_definitions.add(validation_definition)
        validation_result = validation_definition.run(
            batch_parameters={"dataframe": df}
        )
        result = validation_result.to_json_dict()
        result["implementation"] = "Great Expectations Core"
        result["suite_name"] = SUITE_NAME
        result["success"] = bool(validation_result.success)
    except Exception as exc:
        result = {
            "implementation": "Great Expectations Core",
            "suite_name": SUITE_NAME,
            "success": False,
            "error": repr(exc),
            "note": "Install requirements.txt and rerun; do not treat this exception as a passed validation.",
        }
    Path(output_json).write_text(json.dumps(result, indent=2, default=str), encoding="utf-8")
    return result
