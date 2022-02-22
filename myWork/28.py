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

# from abc import ABC, abstractmethod
#
#
# class Transport(ABC):
#     """
#     Абстракный класс, его нельзя присвоить к экземпляру
#     """
#
#     def __init__(self, color: str, speed: int) -> None:
#         self.color = color
#         self.speed = speed
#         self.move = False
#
#     @abstractmethod
#     def signal(self):
#         pass
#
#
# class MoveEarth(Transport):
#     def signal(self):
#         print('Транспорт подал сигнал')
#
#     def __init__(self, color: str, speed: int):
#         super().__init__(color, speed)
#         self.move_earth = False
#
#     def move_to_earth(self):
#         self.move_earth = True
#         print('Транспорт начал движение по земле')
#
#
# class Music:
#     def __init__(self):
#         self.music = True
#
#
# class MoveWater(Transport):
#     def signal(self):
#         print('Транспорт подал сигнал')
#
#     def __init__(self, color: str, speed: int):
#         super().__init__(color, speed)
#         self.move_water = False
#
#     def move_to(self):
#         self.move_water = True
#         print('Транспорт начал движение по воде')
#
#
# class Amphibian(MoveWater, MoveEarth, Music):
#     def __init__(self, color: str, speed: int, music):
#         super().__init__(color, speed)
#         self.name = 'Амфибия'
#         self.music = music
#
#
# a = MoveEarth(color='red', speed=160)
# a.signal()
# b = Amphibian('Blue', 100, False)
# print(b.music)


#######################################################################
from abc import ABC, abstractmethod

#
# class Figure(ABC):
#     """sdf"""
#     def __init__(self, x: int, y: int, l: int, w: int):
#         self.x = x
#         self.y = y
#         self.l = l
#         self.w = w
#
#     @abstractmethod
#     def move(self, x: int, y: int) -> None:
#         self.x = x
#         self.y = y
#
#
# class ResizableMixin:
#     def resize(self, l: int, w: int) -> None:
#         self.l = l
#         self.w = w
#
#
# class Square(Figure, ResizableMixin):
#     def __init__(self, x: int, y: int, l: int):
#         super().__init__(x, y, l, l)
#
#
# a = Square(x=10, y=20, l=5)
# for figure in [a]:
#     new_size_x = figure.l * 2
#     new_size_y = figure.w * 2
#     figure.resize(new_size_x, new_size_y)


# 28.5 Класс как контекст-менеджер. Методы enter и exit
# Задача 1. Работа с файлом
#
# Реализуйте класс File — контекстный менеджер для работы с файлами. Он должен принимать
# на вход имя файла и режим чтения/записи и открывать сам файл. В начале работы менеджер
# возвращает файловый объект, а в конце — закрывает файл.
#
# Пример основного кода:
#
# with File(‘example.txt’, ‘w’) as file:
#     file.write(‘Всем привет!’)


# class File:
#     def __init__(self, name, read_write):
#         self. name = name
#         self.read_write = read_write
#
#     def __enter__(self):
#         self.file = open(self.name, self.read_write, encoding='utf-8')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with File('example.txt', 'w') as file:
#     file.write('Всем привет!')





# 28.6 Методы класса: декораторы setter и property
#
# Задача 1. Транспорт 2


# class Person():
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def __str__(self):
#         return ' '.join([self._name, str(self._age)])
#
#     def getter_name(self):
#         return self._name
#
#     def setter_name(self, name):
#         self._name = name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, a):
#         if a < 0:
#             raise Exception('Недопустимый возраст')
#         else:
#             self._age = a
#             return self._age
#
#
# tom = Person('Tom', 26)
# print(tom)
# print(tom.age)
# tom.age = -100
# print(tom.age)
# print(tom)




