class Man:

    def father(self):
        print("I'm your father!")

class Woman:

    def mother(self):
        print("I'm your mother!")


#child 类同时具有Man 和 Woman 两个类的属性和方法
class child(Woman,Man):

    def son(self):
        print("We are happy family!")

tianyou = child()
tianyou.father()
tianyou.mother()
tianyou.son()