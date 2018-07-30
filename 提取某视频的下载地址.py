#解决该网战迅雷无法批量下载的问题，直接得到所有下载地址
'''
import sys
if len(sys.arfv) < 2:
    print("用法： python 本文件名加目标网址")
    exit()
url = sys.argv[1]
'''
from bs4 import BeautifulSoup
import requests
url = 'https://www.77kp.com/vod-detail-id-88283.html'   #要提取地址的网页

html = requests.get(url).text
sp = BeautifulSoup(html,'html.parser')
all_links = sp.find_all('a')                        #html中链接的标签是'a'

for link in all_links:
    href = link.get('href')
    if href != None and href.startswith('thunder://'):
        print(href)