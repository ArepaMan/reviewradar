import pandas as pd

from reviewradar.data.clean import clean_text
from reviewradar.data.duplicates import drop_duplicates_texts
from reviewradar.data.overlap import remove_overlap


def clean_splits(train_df: pd.DataFrame, test_df: pd.DataFrame):

    train_df = train_df.assign(text=train_df["text"].apply(clean_text))
    test_df = test_df.assign(text=test_df["text"].apply(clean_text))
    train_df = remove_overlap(train_df, test_df)
    train_df = drop_duplicates_texts(train_df)
    return train_df.reset_index(drop=True), test_df.reset_index(drop=True)
