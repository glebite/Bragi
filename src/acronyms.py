#!/usr/bin/env python3
"""
"""
import textract
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import copy
# import sys


def main(arguments):
    pass


if __name__ == "__main__":
    textContents = textract.process('../data/rfc3261.txt.pdf',
                         method='pdfminer').decode("utf8")
    stop_words = set(stopwords.words('english'))

    print(textContents)
    
    # words = word_tokenize(textContents)

    # for pos, word in enumerate(words):
    #     # print(word)
    #     # print(f'Pos: {pos} word: {word}')
    #     if '(' in word:
    #         print(f'\tBird: {word} {words[pos+1]} {words[pos+2]}')
    #     # if '(' in word:
    #     #     print(word)
    #     #     # print(f'\t{pos} >>{x[0][pos-1]}<<')
