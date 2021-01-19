from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy
import jieba
import pymongo

client = pymongo.MongoClient('mongodb://admin:123456@10.117.9.213:27017/')

db = client["zxk_test_db"]
mycol = db["zongheng"]       # 查询表名


key = "FictionClass1"

result = mycol.find({key: {"$ne": 'a'}}, {key: 1, "_id": 0})  # 查询key不为a的数据，并且只返回key

txt = ''
for r in result:
    txt += r[key].strip()

wordlist = jieba.cut(txt)
ptxt = ' '.join(wordlist)

image = numpy.array(Image.open('Girl.png'))
wc = WordCloud(background_color='white', max_words=500, mask=image, max_font_size=60, font_path='FangSong_GB2312.ttf').generate(ptxt)

plt.imshow(wc)
plt.axis("off")
plt.show()
