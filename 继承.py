class Person:

    def run(self):
        print("I can run fast!")

    def eat(self):
        print("I eat very much every day,but I will not be fat!")


class Me(Person):

    def study(self):
        print("I can study something qucikly!")

zhuzhiwei = Me()
zhuzhiwei.run()
zhuzhiwei.eat()
zhuzhiwei.study()