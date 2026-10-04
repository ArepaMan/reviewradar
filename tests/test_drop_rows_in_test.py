import pandas as pd

from reviewradar.data.overlap import remove_overlap


def test_remove_overlap():
    train_df = pd.DataFrame(
        {
            "text": [
                "\nWhere can I withdraw money from?\n",
                "how do I reset my password?",
                "What is the interest rate on savings accounts?",
            ],
            "category": ["atm_support", "password_reset", "savings_account"],
        }
    )
    test_df = pd.DataFrame(
        {
            "text": [
                "Where can I withdraw money from?",
                "How do I reset my password?",
            ],
            "category": ["atm_support", "password_reset"],
        }
    )
    expected_df = pd.DataFrame(
        {
            "text": ["What is the interest rate on savings accounts?"],
            "category": ["savings_account"],
        }
    )
    result_df = remove_overlap(train_df, test_df)
    pd.testing.assert_frame_equal(
        result_df.reset_index(drop=True), expected_df.reset_index(drop=True)
    )
