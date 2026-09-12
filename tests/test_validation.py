import pandas as pd
from pipeline.validation.great_expectations_suite import run_validation

def test_validation_suite_passes_on_valid_fixture():
    rows = 5000
    data = {f"f{i}": [0.0] * rows for i in range(170)}
    data["class"] = ["neg"] * (rows - 50) + ["pos"] * 50
    df = pd.DataFrame(data)
    result = run_validation(df, "/tmp/gx_validation_test.json")
    assert result["success"] is True

def test_validation_rejects_wrong_schema():
    df = pd.DataFrame({"class": ["neg"] * 5000})
    result = run_validation(df, "/tmp/gx_validation_bad.json")
    assert result["success"] is False
