import reviewradar


def test_main_prints_greeting(capsys) -> None:
    reviewradar.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from reviewradar!\n"
