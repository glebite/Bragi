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
        self.wordCloud = ''

    def read(self):
        """read - reads the file in

        :param:  n/a
        :return: n/a
        :throws: MissingFileError
        """
        try:
            self.textContents = str(textract.process(self.fileName))
        except textract.exceptions.MissingFileError as e:
            raise e

    def generate(self):
        """generate - actually creates the word cloud

        :param:  n/a
        :return: n/a
        :throws: n/a
        """
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
        """save

        :param:  fileName - name of the file to write to
        :return: n/a
        :throws: n/a
        """
        self.wordCloud.to_file(fileName)


if __name__ == "__main__":
    x = SimpleWordCloud(sys.argv[1])
    x.read()
    x.generate()
    x.save('output.png')
