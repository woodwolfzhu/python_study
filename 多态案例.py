class Dog(object):

    def __init__(self,name):
        self.name = name

    def game(self):
        print("{}伸着舌头哈哈笑".format(self.name))

class Xiaotianquan(Dog):

    def game(self):
        print("%s 追着孙猴子到处跑！" % self.name)


class Person(object):

    def __init__(self,name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 抚摸着 %s 的头" % (self.name, dog.name))
        dog.game()
# 这里dog.____后面的内容与主程序中调用时传入的参数有关，dog.__ 的属性或方法应包含于参数所属的类



wangcai = Xiaotianquan("雪獒")

tangbohu = Person("唐伯虎")
tangbohu.game_with_dog(wangcai)


