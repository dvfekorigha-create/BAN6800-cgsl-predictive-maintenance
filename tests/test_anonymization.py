import pandas as pd
from pipeline.anonymization.anonymize import anonymize_dataframe

def test_anonymization_drops_pii_and_hashes_ids():
    df = pd.DataFrame({"name": ["A"], "asset_id": ["X1"], "value": [1]})
    out = anonymize_dataframe(df, pii_columns=["name"], identifier_columns=["asset_id"])
    assert "name" not in out.columns
    assert out.loc[0, "asset_id"] != "X1"
    assert len(out.loc[0, "asset_id"]) == 64
