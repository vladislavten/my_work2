#
# 27.2 Функция как объект. Функции высшего порядка
#
# Задача 1. Функции

# def func_2(func, *args, **kwargs):
#     result = func(*args, **kwargs) * func(*args, **kwargs)
#     return result
#
#
# def func_1(x):
#     return x + 10
#
#
# print(func_2(func_1, 10))


# Задача 2. Таймер

# import time


# def timer(func):
#     start_time = time.time()
#     func()
#     end_time = time.time()
#     return round(end_time -start_time, 2)
#
#
# def cubes():
#     lst_cubes = [i ** 3 for i in range(5000000)]
#     return lst_cubes
#
#
# print(timer(cubes))



# 27.3 Декораторы
# Задача 1. Двойной вызов

# from typing import Callable
#
#
# def do_twice(func: Callable) -> Callable:
#     def wrapped_func(*args, **kwargs):
#         value = func(*args, **kwargs)
#         value2 = func(*args, **kwargs)
#         return value, value2
#     return wrapped_func
#
#
# @do_twice
# def greeting(name):
#     print('Привет, {name}!'.format(name=name))

# greeting('Tom')


# Задача 2. Таймер 2

from typing import Callable
import time


def timer(func: Callable):
    def wrapped_func(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        return round(end_time - start_time, 2)
    return wrapped_func()


@timer
def cubes():
    lst_cubes = [i ** 3 for i in range(4000000)]
    print('Готово!')
    return lst_cubes


print(cubes)