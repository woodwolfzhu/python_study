#格式化字符串后面的‘（）’本质上就是元组

# print('%s 的股价是 %.2f，数量是 %d' % ('小米',170,500))
infortupe = ('小米',170,500)
print('%s 的股价是 %.2f，数量是 %d' % infortupe)
print(type(infortupe))


infor = '%s 的股价是 %.2f，数量是 %d' % ('小米',170,500)  #或者直接用infotupe也可以
print(infor)
