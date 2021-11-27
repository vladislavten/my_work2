# 20.2 Кортежи

# Задача 1. Создание кортежей
#

# import random
# a = [random.randint(0, 5) for _ in range(10)]
# a = tuple(a)
# print(a)
# b = [random.randint(-5, 0) for _ in range(10)]
# b = tuple(b)
# print(b)
# c = a + b
# print(c)
# print(c.count(0))


# Задача 2. Цилиндр

# import math
# def func(r, h):
#     S = math.pi * r ** 2
#     side = 2 * math.pi * r * h
#     full = side + 2 * S
#     return round(side, 2), round(full, 2)
#
# r = int(input('Введите радиус цилиндра: '))
# h = int(input('Введите высоту цилиндра: '))
#
# cort = func(r, h)
# print(cort[0])
# print(cort[1])
#
#

# Задача 3. Неправильный код
#
# import random
#
# def change(nums):
#
#     index = random.randint(0, 5)
#     value = random.randint(100, 1000)
#     nums = list(nums)
#     nums[index] = value
#     nums = tuple(nums)
#     return nums, value
#
# my_nums = 1, 2, 3, 4, 5
#
# new_nums, rand_val = change(my_nums)
# print(new_nums, rand_val)
#
# new_nums, rand_val2 = change(new_nums)
# rand_val2 += rand_val
# print(new_nums, rand_val2)



# 20.3 Функция enumerate. Перебор нескольких значений

# Задача 1. Саботаж!
# Строка: so~mec~od~e
# string = input('Строка: ')
# result = []
# for index, tilda in enumerate(string):
#     if tilda == '~':
#         result += str(index)
# print('Ответ:', ' '.join(result))


# Задача 2. Словари из списков

import random
def DIC(lst):
    dic = dict()
    for index, values in enumerate(lst):
        dic[index] = values
    return dic


alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
frs = [alphabet[random.randint(0,32)] for _ in range(10)]
sec = [alphabet[random.randint(0,32)] for _ in range(10)]

print('Первая строка', frs)
print('Вторая строка', sec)

frsD = DIC(frs)
secD = DIC(sec)

print('Первый словарь:', frsD)
print('Второй словарь:', secD)
