#!/usr/bin/env python
"""
simple_word_cloud.py
"""
import matplotlib .pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import textract
import sys


class SimpleWordCloud:
    """SimpleWordCloud
    """
    def __init__(self, fileName=None):
        """__init__

        :param:  fileName
        :return: n/a
        :throws: n/a
        """
        self.fileName = fileName
        self.textContents = None
        self.wordCloud = ""

    def read(self):
        """read - reads the file in

        :param:  n/a
        :return: n/a
        :throws: Exception
        """
        try:
            self.textContents = str(textract.process(self.fileName))
        except Exception as e:
            raise e

    def generate(self):
        temp = WordCloud(relative_scaling=1.0,
                         stopwords=set(STOPWORDS))
        self.wordCloud = temp.generate(self.textContents)

    def show(self):
        """show - show the word cloud with plt
        """
        plt.imshow(self.wordCloud)
        plt.axis('off')
        plt.show()


    def save(self, fileName):
        """
        """
        self.wordCloud.to_file(fileName)


if __name__ == "__main__":
    x = WordCloud(sys.argv[1])
    x.read()
    x.generate()
    x.show()