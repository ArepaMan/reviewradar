import pandas as pd

from reviewradar.data.duplicates import make_key


def remove_overlap(train_df: pd.DataFrame, test_df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows from train_df whose text is also in test_df, ignoring edge whitespace and case."""
    train_key = make_key(train_df["text"])
    test_key = make_key(test_df["text"])
    return train_df[~train_key.isin(test_key)]
