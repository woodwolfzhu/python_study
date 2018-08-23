class Person:

    def run(self):
        print("I can run fast!")

    def eat(self):
         print("I eat very much every day,but I will not be fat!")


class Me(Person):

    def __study(self):
        print("I can study something qucikly!")

    def run(self):
        print("I want to zhui houhuimin!")
        super().run()

zhuzhiwei = Me()
zhuzhiwei.run()
zhuzhiwei.eat()
zhuzhiwei._Me__study()