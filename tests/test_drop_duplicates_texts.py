import pandas as pd
import pytest

from reviewradar.data.duplicates import drop_duplicates_texts


def test_drops_duplicate_that_differs_by_newline():
    df = pd.DataFrame(
        {
            "text": [
                "Where can I withdraw money from?",
                "\nWhere can I withdraw money from?",
                "I lost my card",
            ],
            "category": ["atm_support", "atm_support", "lost_or_stolen_card"],
        }
    )
    result = drop_duplicates_texts(df)
    assert len(result) == 2
    assert result["text"].tolist() == [
        "Where can I withdraw money from?",
        "I lost my card",
    ]


def test_drops_duplicate_that_differs_by_case_and_keeps_original_case():
    df = pd.DataFrame(
        {"text": ["How do I top up?", "how do i top up?"], "category": ["a", "a"]}
    )
    result = drop_duplicates_texts(df)
    assert result["text"].tolist() == ["How do I top up?"]


def test_does_not_change_the_input_table():
    df = pd.DataFrame({"text": ["x", "x"], "category": ["a", "a"]})
    drop_duplicates_texts(df)
    assert list(df.columns) == ["text", "category"]
    assert len(df) == 2


def test_same_text_with_different_categories_raises():
    df = pd.DataFrame({"text": ["x", "\nX"], "category": ["a", "b"]})
    with pytest.raises(ValueError):
        drop_duplicates_texts(df)
