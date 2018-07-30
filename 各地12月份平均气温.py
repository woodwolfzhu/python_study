def disp_area():
    i = 0
    for a in second_data:
        print('{:>2}:{:<6}\t'.format(i,a[0]),end='')
        i += 1
        if not(i % 5): print()
    print()
def disp_tempture(num):
    print('当前显示的城市是：{}'.format(num[0]))
    for i in range(1,13):
        print('{}月份的平均气温是：{}'.format(i,float(num[i])))



#主程序
with open('climate.txt','r',encoding='utf-8') as fp:
    first_data = fp.readlines()
second_data = []
for data in first_data:
    second_data.append(data.rstrip('\n').split('\t'))

while True:
    disp_area()
    num = int(input('请输入选择的城市的序号(输入-1退出)：'))
    if num>=0 and num<25:
        disp_tempture(second_data[num])
    elif num == -1:
        break
    else:
        print('您的输入有误请重新输入')
        continue

    x = input('按回车回到主菜单')
;l',.'


