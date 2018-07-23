#书上的程序 必须把3 科成绩全部输完，才能成功运行否则会出错
#增加了try/except 语句，解决上述问题
#对各科的成绩进行了总结
#利用http://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p08_calculating_with_dict.html的方法还可以进行优化
#最大值最小值那好像可以直接求取，好好看上面网站的内容
import os
import operator
students = {}
chinese_score = {}
math_score = {}
english_score = {}
subjects = ['语文','数学','英语']
scores = [chinese_score,math_score,english_score]

def menu():
    print('欢迎使用学生成绩管理系统')
    print('1.  添加学生基本信息')
    print('2.  输入语文成绩')
    print('3.  输入数学成绩')
    print('4.  输入英语成绩')
    print('5.  查看学生成绩')
    print('6.  查看各学科情况')
    print('0.  结束程序')

def add_stuent():
    os.system('cls')
    while True:
        no = int(input('请输入学生学号（输入0结束）：'))
        if no > 0:
            students[no] = input('请输入学生姓名：')
            print(students)
        else:
            break

def add_scores(no_subject):
    os.system('cls')
    for no,name in students.items():
        scores[no_subject][no] = int(input('{},{}的{}成绩是：'.format(no,name,subjects[no_subject])))
    print(scores[no_subject])
    x = input('按回车返回主菜单')

def display_scores():
    os.system('cls')
    print('学生的成绩是：')
    for no,name in students.items():
        sum = 0
        print('{}: {}的成绩是：'.format(no,name),end="")
        for no_subject in range(3):
            try:
                sum = sum + scores[no_subject][no]
                print('{}：{}  \t'.format(subjects[no_subject],scores[no_subject][no]),end="")
            except KeyError:
                scores[no_subject][no] = 0
                sum = sum + scores[no_subject][no]
                print('{}：{}  \t'.format(subjects[no_subject], scores[no_subject][no]), end="")
        print("总分是：{}  平均分是：{:.2f}".format(sum,sum/3))                #{}中的":.2f"使得结果保留两位小数
    x = input('按回车回到主菜单')

def total():
    for a in range(3):
        try:
            max_score = max(zip(scores[a].values()))#执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器
            min_score = min(zip(scores[a].values()))
        except:
            max_score,min_score = 0,0
        print('{}最高成绩是：{}  最低成绩是{}  '.format(subjects[a],max_score,min_score),end='')
        sum = 0
        n = 0
        for key,value in scores[a].items():
            try:
                sum = sum + value
                n = n+1
            except KeyError:
                value = 0
                sum = sum + value
                n = n+1
        if n == 0:
            n = 1
        print("平均成绩为：{:.2f}".format(sum/n))


while True:
    os.system('cls')
    menu()
    n = int(input())
    if n == 1:
        add_stuent()
    elif n>1 and n<5:
        add_scores(n-2)
    elif n == 5:
        display_scores()
    elif n == 6:
        total()
    else:
        break


