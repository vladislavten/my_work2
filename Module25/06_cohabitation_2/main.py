from random import choice


class House:
    __money = 100
    __food = 50
    __cat_food = 30
    __dirt = 0
    __total_food = 0

    def set_husband_money(self):
        self.__money += 150

    def set_wife_money(self, spend):
        self.__money -= spend

    def set_food(self, food):
        self.__food += food

    def set_clean(self, clean):
        self.__dirt -= clean

    def set_dirt(self):
        self.__dirt += 5

    def set_minus_food(self, minus_food):
        self.__food -= minus_food
        self.__total_food += minus_food

    def get_total_food(self):
        return self.__total_food

    def get_food(self):
        return self.__food

    def get_money(self):
        return self.__money

    def get_dirt(self):
        return self.__dirt


house = House()


class Person:
    def __init__(self, name, hungry=30, happy=100):
        self.__name = name
        self.__hungry = hungry
        self.__happy = happy

    def eat(self, eat):
        self.__hungry += eat
        house.set_minus_food(eat)

    def caress_the_cat(self):
        self.__happy += 5

    def get_name(self):
        return self.__name

    def get_hungry(self):
        return self.__hungry

    def get_happy(self):
        return self.__happy

    def set_hungry(self):
        self.__hungry -= 10

    def set_happy_plus(self):
        self.__happy += 20

    def set_happy_minus(self):
        self.__happy -= 10


class Husband(Person):
    __money = 0

    def __init__(self, name):
        super().__init__(name)

    def play(self):
        self.set_hungry()
        self.set_happy_plus()

    def go_to_work(self):
        self.set_hungry()
        house.set_husband_money()
        self.__money += 150

    def get_money(self):
        return self.__money


class Wife(Person):
    __total_coat = 0

    def __init__(self, name):
        super().__init__(name)

    def buy_goods(self, money):
        self.set_hungry()
        house.set_wife_money(money)
        house.set_food(money)

    def buy_coat(self, money):
        self.set_hungry()
        house.set_wife_money(money)
        self.__total_coat += 1

    def clean_house(self, clean):
        self.set_hungry()
        house.set_clean(clean)

    def get_total_coat(self):
        return self.__total_coat


class Cat:
    def __init__(self, cat_name, cat_hungry=30):
        self.cat_name = cat_name
        self.__cat_hungry = cat_hungry

    def eat(self):
        self.__cat_hungry += 20
        house.set_food(10)

    def sleep(self):
        self.__cat_hungry -= 10

    def break_the_wall(self):
        self.__cat_hungry -= 10
        house.set_dirt()

    def get_name(self):
        return self.cat_name

    def get_hungry(self):
        return self.__cat_hungry


wife = Wife('Ульяна')
husband = Husband('Владислав')
cat = Cat('Барсик')

days = 365

while days > 0:
    days -= 1
    house.set_dirt()
    if husband.get_hungry() <= 0 or wife.get_hungry() <= 0 or cat.get_hungry() <= 0:
        print('Член семьи умер от голода')
        break

    if husband.get_happy() <= 10 or wife.get_happy() <= 10:
        print('Член семьи умер от диспрессии')
        break

    if house.get_dirt() >= 90:
        husband.set_happy_minus()
        wife.set_happy_minus()

    if husband.get_hungry() <= 10:
        if house.get_food() > 30:
            husband.eat(30)
        elif house.get_food() < 30:
            husband.eat(house.get_food())

    if wife.get_hungry() <= 10:
        if house.get_food() > 30:
            wife.eat(30)
        elif house.get_food() < 30:
            wife.eat(house.get_food())
    husband_choice = choice(['есть', 'работать', 'играть', 'гладить'])
    if husband_choice == 'есть':
        if house.get_food() > 0:
            if husband.get_hungry() < 70:
                husband.eat(30)
            elif husband.get_hungry() > 70:
                husband.eat(100 - husband.get_hungry())
    elif husband_choice == 'работать':
        husband.go_to_work()
    elif husband_choice == 'играть':
        husband.play()
    elif husband_choice == 'гладить':
        husband.caress_the_cat()

    wife_choice = choice(['есть', 'купить еду', 'купить шубу', 'гладить', 'уборка'])
    if wife_choice == 'есть':
        if house.get_food() > 0:
            if wife.get_hungry() < 70:
                wife.eat(30)
            elif wife.get_hungry() > 70:
                wife.eat(100 - wife.get_hungry())
    elif wife_choice == 'купить еду':
        wife.buy_goods(55)  # Прописать для теста 30
    elif wife_choice == 'купить шубу':
        if house.get_money() >= 350:
            wife.buy_coat(350)
    elif wife_choice == 'гладить':
        wife.caress_the_cat()
    elif wife_choice == 'уборка':
        if house.get_dirt() > 100:
            wife.clean_house(100)
        elif 100 > house.get_dirt() > 0:
            wife.clean_house(100 - house.get_dirt())

    cat_choice = choice(['есть', 'спать', 'драть обои'])
    if cat_choice == 'есть':
        cat.eat()
    elif cat_choice == 'спать':
        cat.get_hungry()
    elif cat_choice == 'драть обои':
        cat.break_the_wall()

if days == 0:
    print('Съедено еды за год:', house.get_total_food())
    print('Муж заработал денег:', husband.get_money())
    print('Куплено шуб', wife.get_total_coat())
