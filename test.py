from main import count


def test_main_valid():
    assert count("text.txt") == {'ADVB': 6, 'VERB': 14, 'ADJ': 9}


def test_main_invalid():
    assert count("text1.txt") == {'ADVB': 0, 'VERB': 0, 'ADJ': 0}
