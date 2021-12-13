# 21.2 Рекурсия
# Задача 1. Challenge

# def factorial(num):
#     if num == 1:
#         return 1
#     fac = num * factorial(num - 1)
#     return fac
#
# result = factorial(5)
#
# print(result)


# Задача 2. Степень числа

# def power(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * power(a, n - 1)
#
#
# float_num = float(input('Введите вещественное число: '))
#
# int_num = int(input('Введите степень числа: '))
#
# print(float_num, '**', int_num, '=', power(float_num, int_num))

# Задача 3. Поиск элемента

# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
# def find_key(struct, key):
#     if key in struct:
#         return struct[key]
#     for i in struct.values():
#         if isinstance(i, dict):
#             result = find_key(i, key)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
# find = input('Какой ключ ищем? ')
# result = find_key(site, find)
# if result:
#     print(result)
# else:
#     print('Такого ключа в структуре сайта нет')


# простая рекурсия

# def foo1(start):
#     if start == 0:
#         return
#
#     print(start)
#     (foo1(start - 1))
#
#
# foo1(100)


# 21.3 Передача изменяемых и неизменяемых данных в функцию
# Задача 1. Ошибка
# (ошибка была в том что в функцию передавалась ссылка а нужно чтобы передавалось значение)

# import random
#
# def change_dict(dct):
#     num = random.randint(1, 100)
#     for i_key, i_value in dct.items():
#         if isinstance(i_value, list):
#             i_value.append(num)
#         if isinstance(i_value, dict):
#             i_value[num] = i_key
#         if isinstance(i_value, set):
#             i_value.add(num)
#     return dct
#
#
# nums_list = [1, 2, 3]
#
# some_dict = {1: 'text', 2: 'another text'}
#
# uniq_nums = {1, 2, 3}
#
# common_dict = {1: [1, 2, 3], 2: {1: 'text', 2: 'another text'}, 3: {1, 2, 3}, 4: (10, 20, 30)}
# print(nums_list, '\t', some_dict, '\t', uniq_nums)
# change_dict(common_dict)
# print(nums_list, '\t', some_dict, '\t', uniq_nums)
#
# print(common_dict)


# Задача 2. Непонятно!              https://coderoad.ru/22199741/%D0%9E%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D1%82%D0%B8%D0%BF%D0%B0-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%B2%D1%85%D0%BE%D0%B4%D0%BD%D1%8B%D1%85-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85
# x = input("Введите данные: ")
#
# try:
#     if type(eval(x)) == float:
#         print('Тип данных: Float')
#         print('Неизменяемый (immutable)')
#     elif type(eval(x)) == int:
#         print(x, " is interger number")
#     elif type(eval(x)) == bool:
#         print(x, " is a boolean")
#     elif type(eval(x)) == list:
#         print(x, " is a list")
# except:
#     print('Тип данных: str (строка)')
# print('ID:', id(x))


# 21.4 Именованные аргументы и значения по умолчанию
# Задача 1. Работа с файл

# def ask_user(question,
#              complaint = 'Неверный ввод. Введите да или нет',
#              retries = 4):
#     while True:
#         answer = input(question).lower()
#         if answer == 'да':
#             return 1
#         if answer == 'нет':
#             return 0
#         retries -= 1
#         if retries == 0:
#             print('Количество попыток истекло.')
#             break
#         print(complaint)
#         print('Осталось попыток', retries)
#
# ask_user('Вы действительно хотите выйти? ')
# ask_user('Удалить файл? ', 'Вы точно хотите удалить или нет?')
# ask_user('Записать файл? ')


# Задача 2. Накопление значений

# def add_num(num, lst = []):
#     lst.append(num)
#     print(lst)
#
# add_num(5)
# add_num(10)
# add_num(15)


# Задача 3. Помощь другу

# def create_dict(data, template = dict() ):
#     template = dict()
#     if isinstance(data, dict):
#         return data
#     if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
#         template[data] = data
#         return template
#     if isinstance(data, list) or isinstance(data, set):
#         return ''
#
#
#
# def data_preparation(old_list):
#     new_list = []
#     for i_element in old_list:
#         new_list.append(create_dict(i_element))
#     return new_list
#
# data = ['sad', {'sds': 23}, 99, {43}, [12, 42, 1], 2323]
# data = data_preparation(data)
# print(data)

