class MusicPlayer:

    # 记录第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):
        print("申请内存空间")
        # 1.判断类属性是否是空对象
        if cls.instance is None:

        # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return  cls.instance

player_1 = MusicPlayer()
print(player_1)

player_2 = MusicPlayer()
print(player_2)