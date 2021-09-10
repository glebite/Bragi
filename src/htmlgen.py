#!/usr/bin/env python
"""
htmlgen.py - conversion from PDF or such into html but with some smarts.
"""


class HtmlGen(object):
    """HtmlGen - this is where the magic happens, baby.
    """
    def __init__(self, fileName=None):
        """init
        """
        self.fileName = fileName

    def paragraph(func):
        def wrapper(*args, **kwargs):
            return f'<p>{func(*args, **kwargs)}</p>'
        return wrapper

    def body(func):
        def wrapper(*args, **kwargs):
            return f'<body>{func(*args, **kwargs)}</body>'
        return wrapper

    @paragraph
    def output(self, text):
        return text

    @body
    def otheroutput(self, text):
        return text


if __name__ == "__main__":
    x = HtmlGen()
    print(x.output("whatever"))
