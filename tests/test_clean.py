import pandas as pd
from pipeline.core.clean import fit_transform_train, transform_with_artifact

def test_train_transform_removes_duplicates_and_missing_values():
    df = pd.DataFrame({"class": ["neg", "pos", "neg"], "aa_000": [1, None, 1], "dropme": [None, None, None]})
    out, artifact, stats = fit_transform_train(df, missing_threshold=0.80)
    assert stats["duplicates_removed"] == 1
    assert "dropme" in artifact.dropped_columns
    assert out.isna().sum().sum() == 0
    assert set(out["class"].unique()) == {0, 1}

def test_test_transform_reuses_training_medians():
    train = pd.DataFrame({"class": ["neg", "pos"], "aa_000": [10, 20]})
    test = pd.DataFrame({"class": ["neg"], "aa_000": [None]})
    _, artifact, _ = fit_transform_train(train)
    out, _ = transform_with_artifact(test, artifact)
    assert out.loc[0, "aa_000"] == 15
