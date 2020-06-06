import jieba
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer 
from pymongo import MongoClient





############################
#字典方式使用
client = MongoClient()
collection = client['my_test']['scrapy_qsbk']
data = collection.find()
data_list = list()
for i in data:
    temp = {}
    temp['sex'] = i['sex']
    temp['subs'] = int(i['subs'])
    temp['comment'] = int(i['comment'])
    data_list.append(temp)

dv = DictVectorizer(sparse=False)
data = dv.fit_transform(data_list)
print(dv.get_feature_names())
for i in data:
    print(i)

##########################
f = open('file.txt', 'r', encoding='utf-8') # 打开JS文件
line = f.readline()
htmlstr = ''
while line:
    htmlstr = htmlstr+line
    line = f.readline()
f.close()


res = jieba.cut(htmlstr)
print(res)
res = list(res)
res = " ".join(res)
#print([res])#res为jieba操作过,加了空格的字符串

#res = "There are moments in life when you miss someone so much that you just want to pick them from your dreams and hug them for real! Dream what you want to dream;go where you want to go;be what you want to be,because you have only one life and one chance to do all the things you want to do.May you have enough happiness to make you sweet,enough trials to make you strong,enough sorrow to keep you human,enough hope to make you happy? Always put yourself in others’shoes.If you feel that it hurts you,it probably hurts the other person, too.The happiest of people don’t necessarily have the best of everything;they just make the most of everything that comes along their way.Happiness lies for those who cry,those who hurt, those who have searched,and those who have tried,for only they can appreciate the importance of peoplewho have touched their lives.Love begins with a smile,grows with a kiss and ends with a tear.The brightest future will always be based on a forgotten past, you can’t go on well in lifeuntil you let go of your past failures and heartaches.When you were born,you were crying and everyone around you was smiling.Live your life so that when you die,you're the one who is smiling and everyone around you is crying.Please send this message to those people who mean something to you,to those who have touched your life in one way or another,to those who make you smile when you really need it,to those that make you see the brighter side of things when you are really down,to those who you want to let them know that you appreciate their friendship.And if you don’t, don’t worry,nothing bad will happen to you,you will just miss out on the opportunity to brighten someone’s day with this message."



#count使用
# cv = CountVectorizer()
# data = cv.fit_transform([res])
# print(cv.get_feature_names())
# print(data.toarray())



#tfidf使用
# tf = TfidfVectorizer()
# data = tf.fit_transform([res,'这里 需要 多个 字符串 进行 对比','这是 因为 tfidf 算法 内在 的 要求 决定 的'])
# print(tf.get_feature_names())
# print(data.toarray())

