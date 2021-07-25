#!/usr/bin/env python3
"""
"""
import textract
# from nltk.corpus import stopwords
# from nltk.tokenize import TreebankWordTokenizer

import re
# import sys


def main(arguments):
    pass


if __name__ == "__main__":
    textContents = textract.process('../data/rfc3261.txt.pdf',
                                    method='pdfminer').decode('utf8')
    textContents = textContents.split(' ')
    reducedContents = [word for word in textContents if len(word)]
    for pos, word in enumerate(reducedContents):
        if re.search(r'\([A-Z]*\)', word):
            wordLength = len(word)-3
            print(f'ACRONYM: {word} Definition:'
                  ' {reducedContents[pos-wordLength:pos]}')
