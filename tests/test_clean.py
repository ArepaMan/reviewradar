from reviewradar.data.clean import clean_text


def test_clean_text_strips_newlines():
    assert clean_text("\nHello World\n") == "Hello World"
