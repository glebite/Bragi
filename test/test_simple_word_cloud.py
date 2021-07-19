from src.simple_word_cloud import SimpleWordCloud


def test_creation():
    x = SimpleWordCloud('')
    assert x is not None
