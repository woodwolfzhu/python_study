import re
import operator
fp = open('sample.txt','r') #打开文件
article = fp.read()       #将fp指向的文件的内容赋给article
new_article = re.sub('[^a-zA-Z\s]', '', article)    #涉及到了正则表达式
words = new_article.split()        #split()函数没有参数时以空字符将字符串分割
word_counts = {}       #将其初始化为字典 {}中没有参数
for word in words:
    if word.upper() in word_counts:           #upper()将小写字母转化为大写字母
        word_counts[word.upper()] = word_counts[word.upper()] + 1 #记录单词出现的次数
    else:
        word_counts[word.upper()] = 1 #第一次遇到该单词时执行';l.p[
value_list=sorted(word_counts.items(),key=operator.itemgetter(1))#这里改为按照item的第二个字符排序，即value排序
'''.items()返回d的是以键 和 值 组成的元组的列表'''
value_list.reverse()                           #反转列表顺序，从大到小排列
for value in value_list:
    if value[1] > 1:
        print(value)