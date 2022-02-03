class Person:
    def __init__(self, name, hungry=30, happy=100):
        self.__name = name
        self.__hungry = hungry
        self.__happy = happy

    def eat(self):
        self.__hungry += 30
        House.set_222()

    def caress_the_cat(self):
        self.__happy += 5

    def get_name(self):
        return self.__name

    def set_hungry(self):
        self.__hungry -= 10

    def set_happy(self):
        self.__happy += 20


class Husband(Person):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        self.set_hungry()
        self.set_happy()

    def go_to_work(self):
        self.set_hungry()
        House.set_husband_money()


class Wife(Person):
    def __init__(self, name):
        super().__init__(name)

    def buy_goods(self):
        self.set_hungry()
        House.set_goods()
        House.set_wife_money(10)

    def buy_coat(self):
        self.set_hungry()
        House.set_wife_money(350)

    def clean_house(self):
        self.set_hungry()
        House.set_clean()



class Cat:
    def __init__(self, cat_name, cat_hungry=30):
        self.cat_name = cat_name
        self.cat_hungry = cat_hungry

    def cat_eat(self):
        self.cat_hungry += 10

    def cat_sleep(self):
        self.cat_hungry -= 10

    def break_the_wall(self):
        self.cat_hungry -= 10
        House.set_dirt()


class House:
    __money = 100
    __food = 50
    __cat_food = 30
    __dirt = 0

    def set_husband_money(self):
        self.__money += 150

    def set_wife_money(self, spend):
        self.__money -= spend

    def set_goods(self):
        self.__food += 10

    def set_clean(self):
        self.__dirt += 100

    def set_dirt(self):
        self.__dirt += 5

    def get_111(self):
        print(self.__food)

    def set_222(self):
        self.__food -= 15

a = House()
a.get_111()
cat = Wife('sdf')
a.get_111()

