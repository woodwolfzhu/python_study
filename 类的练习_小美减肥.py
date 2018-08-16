class Person:

    def __init__(self,new_name,new_weight):
        self.name = new_name
        self.weight = int(new_weight)

    def eat(self,num):
        self.weight += int(num)
        print("%s's weight had gain %d kg!" % (self.name,int(num)))

    def run(self,num):
        self.weight -= 0.5 * int(num)
        print("%s's weight had decreased %d kg!" % (self.name,0.5 * int(num)))



xiaoming = Person("huying", 45)
print("my name is {},my weight is {} kg".format(xiaoming.name, xiaoming.weight))
a = input("how many times I had ran?")
b = input("how many times I had ate?")
xiaoming.run(a)
xiaoming.eat(b)
print("My weight is {} kg today!".format(xiaoming.weight))