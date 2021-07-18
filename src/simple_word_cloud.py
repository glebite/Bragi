import matplotlib .pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import textract

# read file here
text = str(textract.process('../data/rfc3261.txt.pdf'))

wordcloud = WordCloud(relative_scaling=1.0,
                      stopwords=set(STOPWORDS)).generate(text)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()
