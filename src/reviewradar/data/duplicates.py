import pandas as pd

from reviewradar.data.clean import clean_text


def make_key(texts: pd.Series) -> pd.Series:
    """Comparison key: stripped and lowercased. Used only for matching."""
    return texts.apply(clean_text).str.lower()


def drop_duplicates_texts(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows whose text repeats an earlier row, ignoring edge whitespace
    and case. Keeps the first row unchanged. Raises ValueError if rows that
    share a key have different categories."""
    key = make_key(df["text"])

    n_labels = df.groupby(key)["category"].nunique()
    conflicts = n_labels[n_labels > 1]
    if not conflicts.empty:
        raise ValueError(
            f"Same text with different categories: {list(conflicts.index)}"
        )

    return df[~key.duplicated(keep="first")]
