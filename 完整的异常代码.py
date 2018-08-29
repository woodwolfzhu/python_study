try:
    num = int(input("请输入一个整数："))
    result = 10 / num
except ValueError:
    print("请输入正确的数字")
except Exception as result:
    print("错误类型是:{}".format(result))
else:
    print("没有错误时执行的代码")
finally:
    print("不论是否有错误均会执行的代码")