#用户输入掷骰子的次数，列出每一个数字出现的百分比
import random
number = {}
n = int(input('请输入要掷的次数：'))
x = 1
for a in range(1,7):
    number[a] = 0
while x<=n:
    num = random.randint(1,6)
    number[num] = number[num] + 1
    x = x+1
print('您总共掷了%d 次' % n)
for a in range(1,7):
    percent = number[a] / n
    print("数字{} 出现的次数是：{} 所占百分比为{:.2%}".format(a,number[a],percent))  #注意百分数的表示方式，和其保留小数的方式



