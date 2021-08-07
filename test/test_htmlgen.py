import pytest
from htmlgen import HtmlGen


@pytest.mark.sanity
@pytest.mark.sunshine
def test_creation():
    x = HtmlGen()
    assert x is not None


def test_p_tagify():
    x = HtmlGen()
    assert x.p_tagify("X") == "<p>X</p>"


def test_output():
    x = HtmlGen()
    assert x.output("whatever") == "<p>whatever</p>"

    
