# 28.2 Множественное наследование: MRO

# Задача 1. Снова роботы
# На военную базу привезли очередную партию роботов. И в этот раз не абы каких, а летающих:
# разведывательного дрона и военного робота.
#
# Разведывательный дрон просто летает в поиске противника.
# При команде operate он выводит сообщение «Веду разведку с воздуха» и передвигается немного вперёд.
#
# У летающего военного робота есть оружие, и при команде operate он выводит сообщение о защите военного
# объекта с воздуха с помощью этого оружия.
#
# Напишите программу, которая реализует все необходимые классы роботов. Сущности «Робот» и «Может летать»
# должны быть вынесены в отдельные классы. Обычный робот имеет модель и может вывести сообщение «Я — Робот».
# Объект, который умеет летать, дополнительно имеет атрибуты «Высота» и «Скорость», а также может взлетать,
# летать и приземляться.

# class Robot:
#     """Базовая модель класса Робот"""
#     def __init__(self, model: str):
#         self.model = model
#
#     def say(self):
#         print(f'Я робот {self.model}')
#
#
# class Fly:
#     @staticmethod
#     def can_fly():
#         print('Я полетел')
#
#
# class Fly_robot(Robot, Fly):
#     def __init__(self, model: str, height: bool, speed: int):
#         super().__init__(model)
#         self.height = height
#         self.speed = speed
#
#     def fly_up(self):
#         self.height = True
#         print('Я взлетел. Мой статус: {}'.format(self.height))
#
#     def fly_down(self):
#         self.height = False
#         print('Я приземлился. Мой статус: {}'.format(self.height))
#
#
# basic_robot = Robot('Xr34')
# basic_robot.say()
#
# warrior_robot = Fly_robot('XC35', False, 120)
# warrior_robot.say()
# warrior_robot.can_fly()
# warrior_robot.fly_up()
# warrior_robot.fly_down()


# 28.4 Множественное наследование: примеси и абстрактные классы

# Задача 1. Транспорт
#
# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость,
# и каждый умеет двигаться и подавать сигнал. В парке транспорта стоят:
#
# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.
# Напишите код, который реализует соответствующие классы и методы.\
# Класс «Транспорт» должен быть абстрактным и содержать абстрактные методы.
#
# Также добавьте класс-примесь, в котором реализован функционал проигрывания музыки.
# «Замешайте» этот класс в «Амфибию»

from abc import ABC, abstractmethod


class Transport(ABC):
    """
    Абстракный класс, его нельзя присвоить к экземпляру
    """

    def __init__(self, color: str, speed: int) -> None:
        self.color = color
        self.speed = speed
        self.move = False

    @abstractmethod
    def signal(self):
        print('Транспорт подал сигнал')


class MoveEarth(Transport):
    def __init__(self, color: str, speed: int):
        super().__init__(color, speed)
        self.move_earth = False

    def move_to_earth(self):
        self.move_earth = True
        print('Транспорт начал движение по земле')


#
# class MoveWater(Transport, ABC):
#     def __init__(self, color: str, speed: int):
#         super().__init__(color, speed)
#         self.move_water = False
#
#     def move_to(self):
#         self.move_water = True
#         print('Транспорт начал движение по воде')
#
#
# class Amphibian(MoveWater, MoveEarth, ABC):
#     def __init__(self, color: str, speed: int):
#         super().__init__(color, speed)
#         self.name = 'Амфибия'


a = MoveEarth(color='red', speed=160)
a.signal()
print(a.color)
