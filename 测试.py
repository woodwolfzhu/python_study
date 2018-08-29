def demo1():
    return int(input("输入整数："))

def demo2():
    return  demo1()


print(demo2())