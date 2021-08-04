#!/usr/bin/env python
"""
"""
from functools import wraps


class HtmlGen(object):
    """
    """
    def __init__(self):
        """
        """
        pass

    def paragraph(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<b>{func(*args, **kwargs)}</b>'
        return wrapper
    
    def p_tagify(self, text):
        """p_tagify - wrap with p
        """
        return f'<p>{text}</p>'

    def body_tagify(self, text):
        """body_tagify - wrap with body
        """
        return f'<body>{text}</body>'

    @paragraph
    def output(self, text):
        return text

if __name__ == "__main__":
    x = HtmlGen()
    x.output("whatever")
