class Game():

    # 历史最高分
    top_score = 0

    def __init__(self,player_name):
        self.player_name = player_name
    # 静态方法
    @staticmethod
    def show_help():
        print("帮助信息：帮助僵尸吃掉你的脑子！")

    # 类方法
    @classmethod
    def show_top_score(cls):
        print("你的历史最高分是：{}".format(cls.top_score))

    def start_game(self):
        print("{} hello".format(self.player_name))
        print("Now the game is begin")

# 1.查看游戏的帮助信息
Game.show_help()

# 2.查看历史最高分
Game.show_top_score()

# 3.创建游戏对象
game = Game("阿呆")
game.start_game()