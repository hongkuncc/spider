# encoding:utf-8
import matplotlib.pyplot as plt
from wordcloud import  WordCloud
import jieba

text_path=open(r'2.txt').read()

word_list=jieba.cut(text_path,cut_all=True)
word_split=" ".join(word_list)
my_wordcloud=WordCloud(font_path="simsun.ttf").generate(word_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()