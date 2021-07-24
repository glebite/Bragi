#!/usr/bin/env python3
"""
"""
import textract
from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
import re
# import sys


def main(arguments):
    pass


if __name__ == "__main__":
    textContents = re.findall(r'\w+|(\(\w+\))+',
                              textract.process('../data/rfc3261.txt.pdf',
                                               method='pdfminer').decode("utf8"))
    stop_words = set(stopwords.words('english'))

    for word in textContents:
        if '(' in word:
            print(word)
