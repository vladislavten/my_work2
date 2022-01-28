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

class Person:
    __count = 0

    def __init__(self, name, age):
        self.set_age(age)
        self.set_name(name)
        Person.__count += 1

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def set_age(self, age):
        if age in range(0, 100):
            self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


man = Person('Вася', 56)

print(man.get_name(), man.get_age())  # Получение данных ГЕТТЕРОМ
old = 15
man.set_age(old)  # Замена возраста СЕТТЕРОМ
print(man.get_name(), man.get_age())

man._Person__age = 10  # Замена возраста у скрытого объекта
print(man.get_name(), man.get_age())

new_name = 'Вова'
man.set_name(new_name)  # Замена имени СЕТТЕРОМ
print(man.get_name(), man.get_age())
