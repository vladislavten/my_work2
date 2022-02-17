#
# 27.2 Функция как объект. Функции высшего порядка
#
# Задача 1. Функции

def func_2(func, *args, **kwargs):
    result = func(*args, **kwargs) * func(*args, **kwargs)
    return result


def func_1(x):
    return x + 10


print(func_2(func_1, 10))


