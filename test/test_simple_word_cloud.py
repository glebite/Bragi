import pytest
import textract
from src.simple_word_cloud import SimpleWordCloud


def test_creation():
    x = SimpleWordCloud('')
    assert x is not None
    assert x.fileName == ''
    assert x.textContents is None
    assert x.wordCloud == ''


def test_read_bad_file():
    with pytest.raises(textract.exceptions.MissingFileError):
        SimpleWordCloud('').read()


def test_read_good_file():
    try:
        SimpleWordCloud('./data/rfc3261.txt.pdf').read()
        assert True
    except textract.exceptions.MissingFileError:
        assert False
