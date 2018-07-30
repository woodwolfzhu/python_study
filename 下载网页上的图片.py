from bs4 import BeautifulSoup
import requests
import sys
import os
from urllib.parse import urlparse
from urllib.request import urlopen

if len(sys.argv) < 2:
    print('用法：python 当前程序的文件名 《target url》')
    exit(1)

url = sys.argv[1]                                              #通过命令窗运行时传入参数
domain = "{}://{}".format(urlparse(url).scheme,urlparse(url).hostname) #使用urlparse模块找出目标网页的主机网址
html = requests.get(url).text                #提取网页的数据，转换成文本文件后放在字符串变量中
sp = BeautifulSoup(html,'html.parser')                 #利用b~对字符串进行解析
all_links = sp.find_all(['a','img'])                   #找出sp变量中标签为 a 和 img 的全部内容


for link in all_links:
    src = link.get('src')                              #<img>的标准链接内容是src
    href = link.get('href')                             #提取此链接中的实际网址  <a>的标准链接内容是href
    targets = [src,href]
    for t in targets:
        if t != None and ('.jpg' in t or '.png' in t):
            if t.startswith('https'):fill_path = t
            else:                   full_path = domain
            print(full_path)
            image_dir = url.split('/')[-1]
            if not os.path.exists(image_dir): os.mkdir(image_dir) #检查目录是否存在，不存在就创建
            filename = full_path.split('/')[-1]
            ext = filename.split('.')[-1]
            filename = filename.split('.')[-2]
            if 'jpg' in ext: filename = filename + '.jpg'
            else:            filename = filename + '.png'
            image = urlopen(full_path)
            fp = open(os.path.join(image_dir,filename),'wb')
            fp.write(image.read())
            fp.close()