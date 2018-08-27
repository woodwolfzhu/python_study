class classmethod:

    num = 0

    def __init__(self):
        classmethod.num += 1

    @classmethod
    def showtime(cls):
        cls.num += 1
        print(cls.num)

a = classmethod()
b = classmethod()
c = classmethod()
print(a)
classmethod.showtime()
classmethod.showtime()
classmethod.showtime()