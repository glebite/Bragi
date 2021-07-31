import pytest
from htmlgen import HtmlGen

@pytest.mark.sanity
@pytest.mark.sunshine
def test_creation():
    x = HtmlGen()
    assert x is not None

