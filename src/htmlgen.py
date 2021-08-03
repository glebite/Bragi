#!/usr/bin/env python
"""
"""


class HtmlGen(object):
    """
    """
    def __init__(self):
        """
        """
        pass

    def p_tagify(self, text):
        """p_tagify - wrap with p
        """
        return f'<p>{text}</p>'

    def body_tagify(self, text):
        """body_tagify - wrap with body
        """
        return f'<body>{text}</body>'


if __name__ == "__main__":
    pass
