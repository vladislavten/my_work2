import math


class Automobile:
    place = 20
    money = 0

    def __init__(self, x_coordinate, y_coordinate, injection):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.injection = injection

    def move(self, dist):
        self.x_coordinate += dist * math.cos(self.injection)
        self.y_coordinate += dist * math.sin(self.injection)
        print(f'Автомобиль отправился по координатам {self.x_coordinate}, {self.y_coordinate}')


class Bus(Automobile):
    def __init__(self, x_coordinate, y_coordinate, injection):
        super().__init__(x_coordinate, y_coordinate, injection)

    def get_in(self, passenger):
        self.place -= passenger
        cost = 50
        self.money += cost * passenger
        print(f'вошли в автобус {passenger} человек, денег в кассе {self.money}')
        print(f'осталось {self.place} мест ')

    def get_out(self, passenger):
        self.place += passenger
        print(f'мест {self.place} осталось ')


volvo = Bus(50, 1, 10)
volvo.move(87)
volvo.get_in(5)
volvo.get_in(5)
volvo.get_in(5)
volvo.move(90)
volvo.get_out(5)
