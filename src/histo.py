#!/usr/bin/env python3
"""
"""
import textract
from collections import Counter
# from wordcloud import STOPWORDS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
# import sys


def main(arguments):
    pass


if __name__ == "__main__":
    textContents = re.findall(r'\w+',
                              str(textract.process('../data/rfc3261.txt.pdf')))
    stop_words = set(stopwords.words('english'))
    word_tokens = [word_tokenize(sent) for sent in textContents]
    print(Counter(textContents).most_common(10))
