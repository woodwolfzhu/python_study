#https://blog.csdn.net/voidfaceless/article/details/78219678
#要在anaconda命令行中使用
import sys
a = sys.argv
print(a)

#书上范例程序
# _*_ coding: utf-8 _*_
#程序 8-4.py (Python 3 version)

import sys

if len(sys.argv)<2:                  #如果sys.argv 的长度小于2，证明是用户忘记了输入该有的参数
    print("使用方法：python 8-4.py 成绩文件")
    exit(1)

no=1
scores=dict()
while True:
    score = int(input('请输入第{}号的成绩:(-1结束)'.format(no)))
    if score == -1: break;
    scores[no] = score
    no += 1

with open(sys.argv[1],'w') as fp:         #也就是说不需要用变量来保存sys.argv的值
    fp.write(str(scores))
print("{}已存储完毕".format(sys.argv[1]))
