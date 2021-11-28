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

# import random
# def DIC(lst):
#     dic = dict()
#     for index, values in enumerate(lst):
#         dic[index] = values
#     return dic
#
#
# alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
#             'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# frs = [alphabet[random.randint(0,32)] for _ in range(10)]
# sec = [alphabet[random.randint(0,32)] for _ in range(10)]
#
# print('Первая строка', frs)
# print('Вторая строка', sec)
#
# frsD = DIC(frs)
# secD = DIC(sec)
#
# print('Первый словарь:', frsD)
# print('Второй словарь:', secD)



# 20.4 Перебор ключей и значений в словаре. Метод items

# Задача 1. Кризис миновал

# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
#             }
#
# for name, price in incomes.items():
#     print(name, '--', price)

# Задача 2. Сервер

#
# server_data = {
#
#     "server": {
#
#         "host": "127.0.0.1",
#
#         "port": "10"
#
#     },
#
#     "configuration": {
#
#         "access": "true",
#
#         "login": "Ivan",
#
#         "password": "qwerty"
#
#     }
#
# }
#
# for name in server_data:
#     print(name)
#     for key in server_data[name]:
#         print('   ', key,':', server_data[name][key])


# Задача 3. В одну строчку

# print([values for i_key, values in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])



# 20.5 Составные ключи

# Задача 1. Паспортные данные

# data = {
#
#     (5000, 123456): ('Иванов', 'Василий'),
#     (6000, 111111): ('Иванов', 'Петр'),
#     (7000, 222222): ('Медведев', 'Алексей'),
#     (8000, 333333): ('Алексеев', 'Георгий'),
#     (9000, 444444): ('Георгиева', 'Мария')
#         }
#
# number = int(input('Введите номер паспорта: '))
# seriya = int(input('Введите серию паспорта: '))
# flg = False
# for index, value in data.items():
#     if number in index and seriya in index:
#         print(f'Данные {number} - {seriya} пренадлежат',' '.join(value))
#         flg = True
# if flg == False:
#     print('Совпадений не найдено')


# Задача 2. Контакты 2

# phonebook = dict()
# while True:
#     IF = input('\nВведите Имя Фамилию через пробел: ').split()
#     phonenumber = input('Введите номер телефона: ')
#     IF = tuple(IF)
#
#
#     if IF in phonebook:
#         print('Такое имя и фамилия уже есть в телефонной книге')
#         choice = input('Хотите заменить? Да/Нет  ')
#         if choice == 'Да' or choice == 'да':
#             phonebook[IF] = phonenumber
#     else:
#         phonebook[IF] = phonenumber
#
#
#     print('\n',phonebook)

