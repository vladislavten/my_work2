# 25.2 Инкапсуляция и сокрытие данных. Геттеры и сеттеры

# Задача 1. Координаты точки

# class Point:
#     def __init__(self, x=0, y=0):
#         self.set_x(x)
#         self.set_y(y)
#
#     def __str__(self):
#         return f'Х = {self.__x} Y = {self.__y}'
#
#     def set_x(self, x):
#         if isinstance(x, int):
#             self.__x = x
#         else:
#             raise Exception('Ошибка ввода')
#
#     def set_y(self, y):
#         if isinstance(y, int):
#             self.__y = y
#         else:
#             raise Exception('Ошибка ввода')
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#
# point = Point(10, 5)
# print(point.get_x())


# Задача 2. Человек

# class Person:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.set_age(age)
#         self.set_name(name)
#         Person.__count += 1
#
#     def set_name(self, name):
#         if isinstance(name, str):
#             self.__name = name
#         else:
#             raise Exception('Ошибка имени')
#
#     def set_age(self, age):
#         if age in range(0, 100):
#             self.__age = age
#         else:
#             raise Exception('Ошибка возраста')
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# man = Person('Вася', 56)
#
# print(man.get_name(), man.get_age())  # Получение данных ГЕТТЕРОМ
# old = 15
# man.set_age(old)  # Замена возраста СЕТТЕРОМ
# print(man.get_name(), man.get_age())
#
# man._Person__age = 10  # Замена возраста у скрытого объекта
# print(man.get_name(), man.get_age())
#
# new_name = 'Вова'
# man.set_name(new_name)  # Замена имени СЕТТЕРОМ
# print(man.get_name(), man.get_age())


# 25.3 Наследование

# Задача 2. Роботы

# class Robot:
#     def __init__(self, model):
#         self.model = model
#
#
# class Pil(Robot):
#     def __init__(self, model):
#         super().__init__(model)
#         self.garbage = 0
#
#     def operate(self):
#         print('Начал пылесосить\nЗаполненость мешка для мусора = {}'.format(self.garbage))
#         self.garbage += 1
#
#
# class Ship(Robot):
#     def __init__(self, model):
#         super().__init__(model)
#         self.gun = 'Ракета'
#
#     def operate(self):
#         print('защита объекта с помощью {}'.format(self.gun))
#
#
# pil = Pil('Art3')
# pil.operate()
# pil.operate()
#
# warShip = Ship('Linkor-5')
# warShip.operate()

#
# Задача 3. Кастомные исключения

# class MyOwnException(Exception):
#     pass
#
# try:
#     qwe
#
# except:
#     raise MyOwnException


# 25.4 Полиморфизм

# Задача 1. Юниты

#
# class Unit:
#     def __init__(self):
#         self.health = 100
#
#     def kick_unit(self, damage=0):
#         self.health -= damage
#         print('нанесен урон: {}\n'
#               'Здоровье: {}'.format(damage, self.health))
#
# class Soldier(Unit):
#     def __init__(self):
#         super().__init__()
#
#
# class Person(Unit):
#     def __init__(self):
#         super().__init__()
#
#     def kick_unit(self, damage=0):
#         damage *= 2
#         self.health -= damage
#         print('нанесен урон: {}\n'
#               'Здоровье: {}'.format(damage, self.health))
#
# man = Person()
# man.kick_unit(1)
#
# war = Soldier()
# war.kick_unit(20)


