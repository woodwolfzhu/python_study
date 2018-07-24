import re
import operator
fp = open('sample.txt','r') #打开文件
article = fp.read()       #将fp指向的文件的内容赋给article
new_article = re.sub('[^a-zA-Z\s]', '', article)    #涉及到了正则表达式
words = new_article.split()        #split()函数没有参数时以空字符将字符串分割 括号中的参数是分割的标识符
word_counts = {}       #将其初始化为字典 {}中没有参数
for word in words:
    if word.upper() in word_counts:           #upper()将小写字母转化为大写字母
        word_counts[word.upper()] = word_counts[word.upper()] + 1 #记录单词出现的次数
    else:
        word_counts[word.upper()] = 1 #第一次遇到该单词时执行

key_list = list(word_counts.keys()) #list(word_counts.keys())取出word_counts中的键组成列表
key_list.sort()           #对list的内容进行从小到大的排序
for key in key_list:
    if word_counts[key] > 1:
        print('{}:{}'.format(key, word_counts[key]))
