class HouseItem:

    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name,self.area)


class House:

    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        #存放家具属性
        self.item = []
        #只放家具的名字
        self.item_name = []

    def add_item(self,new_item):
        if new_item.area < self.free_area:
            self.item.append(new_item)
            self.free_area -= new_item.area
            self.item_name.append(new_item.name)
            print("你的BIG HOUSE 中新加了 {},你的房子现在还有{}平米的剩余空间".
                  format(new_item,self.free_area))
        else:
            print("你的房子没有足够的空间摆放！你还有{}的空间！".format(self.free_area))
            return

    def __str__(self):
        return  "你有一套{}，面积是{}，真有钱！".format(self.house_type,self.area)


# 1.  创建家具
bed = HouseItem("席梦思",4)
chest = HouseItem("柜子",5)
table = HouseItem("餐桌",4)

# 创建一个房子
my_house = House("海景别墅",300)
print(bed)
print(chest)
print(table)
print(my_house)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)
print("你的{}，现在有{} 了！".format(my_house.house_type,my_house.item_name))

# 小小的意淫一下，哈哈！