#!/usr/bin/env python
"""
"""
from functools import wraps


class HtmlGen(object):
    """HtmlGen - this is where the magic happens, baby.
    """
    def __init__(self):
        """
        """
        pass

    def paragraph(func):
        def wrapper(*args, **kwargs):
            return f'<p>{func(*args, **kwargs)}</p>'
        return wrapper

    def p_tagify(self, text):
        """p_tagify - wrap with p
        """
        return f'<p>{text}</p>'

    def body(func):
        def wrapper(*args, **kwargs):
            return f'<body>{func(*args, **kwargs)}</body>'
        return wrapper

    def body_tagify(self, text):
        """body_tagify - wrap with body
        """
        return f'<body>{text}</body>'

    @paragraph
    def output(self, text):
        return text


if __name__ == "__main__":
    x = HtmlGen()
    print(x.output("whatever"))
