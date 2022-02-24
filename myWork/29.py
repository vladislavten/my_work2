
# 29.2 Декоратор context manager

# Задача 1. Таймер
#
# Реализуйте функцию (не класс) timer в качестве контекст-менеджера:
# функция должна работать с оператором with и замерять время работы вложенного кода.

# import time
# from contextlib import contextmanager
# from collections.abc import Iterator
#
#
# @contextmanager
# def timer() -> 'Iterator':
#     start = time.time()
#     try:
#         yield
#     except ZeroDivisionError as zero:
#         print(f'Ошибка: {zero}')
#     finally:
#         print(time.time() - start)
#
#
# with timer():
#     lst_cubes = [i ** 3 for i in range(4000000)]




# Задача 2. Директории
#
# Реализуйте функцию in_dir, которая принимает в качестве аргумента путь и
# временно меняет текущую рабочую директорию на новую. Функция должна быть
# контекст-менеджером. Также реализуйте обработку ошибок (например, если такого
# пути не существует). Вне зависимости от результата выполнения контекст-менеджера
# нужно возвращаться в изначальную рабочую директорию.







# 29.3 Декораторы с аргументами

# Задача 1. Повторение кода
#
# В одной из практик вы уже писали декоратор do_twice, который повторяет вызов
# декорируемой функции два раза. В этот раз реализуйте декоратор repeat, который
# повторяет задекорированную функцию уже n раз.


# from typing import Callable
# import functools
#
#
# def do_twice_with_N(pres):
#     """
#     Декоратор с аргументом
#     """
#     def do_twice(func: Callable) -> Callable:
#         @functools.wraps(func)
#         def wrapped_func(*args, **kwargs):
#             for _ in range(pres):
#                 value = func(*args, **kwargs)
#                 return value
#         return wrapped_func
#     return do_twice
#
#
# @do_twice_with_N(pres=2)
# def greeting(name):
#     print('Привет, {name}!'.format(name=name))
#
#
# greeting('Tom')



############################УРОК ИЗ ВИДЕО ###############################

# Декоратор класса

import time
from datetime import datetime
import functools


def createtime(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        print('Время создания инстанса класса:', datetime.utcnow())
        return instance
    return wrapper


@createtime
class Functions:
    def __init__(self, num: int) -> None:
        self.num = num

    def square(self):
        a = [i for i in range(self.num)]
        print(a)
        return a


my_func_1 = Functions(10)














