import pandas as pd

from reviewradar.data.pipeline import clean_splits


def test_clean_splits():
    train = pd.DataFrame(
        {
            "text": [
                "\nWhere can I withdraw money from?",  # dirty copy
                "Where can I withdraw money from?",  # clean copy: a duplicate
                "how do i reset my pin?",  # matches test after cleaning
                "I lost my card",  # unique
            ],
            "category": [
                "atm_support",
                "atm_support",
                "change_pin",
                "lost_or_stolen_card",
            ],
        }
    )
    test = pd.DataFrame(
        {
            "text": ["How do I reset my PIN?\n", "Is there a fee?", "Is there a fee?"],
            "category": ["change_pin", "fees", "fees"],
        }
    )

    train_out, test_out = clean_splits(train, test)

    assert train_out["text"].tolist() == [
        "Where can I withdraw money from?",
        "I lost my card",
    ]  # your turn
    assert test_out["text"].tolist() == [
        "How do I reset my PIN?",
        "Is there a fee?",
        "Is there a fee?",
    ]  # your turn
    assert len(train) == 4  # the inputs were not changed
