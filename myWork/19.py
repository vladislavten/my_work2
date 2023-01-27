
# 19.1 Словарь: основы
#
# Задача 1. Словарь квадратов чисел
#
# num = int(input('Число: '))
# DC = dict()
#
#
# for i in range(1, num + 1):
#     DC[i] = i ** 2
#
# print(DC)



# Задача 2. Студент
#
# info = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ').split()
#
# dct = dict()
#
# dct['Имя'] = info[0]
# dct['Фамилия'] = info[1]
# dct['Город'] = info[2]
# dct['Место учёбы'] = info[3]
# dct['Оценки'] = info[4]
#
#
# for key, value in dct.items():
#     print(f"{key}: {value}")




# Задача 3. Контакты
# name = ''
# phonebook = dict()
# while name != 'стоп':
#     print('\nТекущие контакты на телефоне:')
#
#     for i in phonebook:
#         print(i, phonebook[i])
#
#     name = input('Введите имя: ')
#     if name in phonebook:
#         print('\nТакое имя уже существует')
#     else:
#         number = input('Введите номер: ')
#         phonebook[name] = number


# 19.2 Методы словарей

# Задача 1. Склады
#
# small_storage = {'гвозди': 5000, 'шурупы': 3040, 'саморезы': 2000}
# big_storage = {'доски': 1000, 'балки': 150, 'рейки': 600}
# big_storage.update(small_storage)
#
# name = input('Введите название товара: ')
# test = big_storage.get(name)
# if name in big_storage:
#     print(name, ':', big_storage[name])
# elif test == None:
#     print('Такого товара нет')


# Задача 2. Кризис фруктов

# incomes = {'apple': 5600.20, 'orange': 3500.45, 'banana': 5000.00, 'bergamot': 3700.56, 'durian': 5987.23, 'grapefruit': 300.40, 'peach': 10000.50, 'pear': 1020.00, 'persimmon': 310.00}
#
# print('\nОбщий доход за год составил', sum(incomes.values()))
# print(incomes)
#
# name = ''
# val = max(incomes.values())
#
# for i in incomes:
#     if incomes[i] < val:
#         val = incomes[i]
#         name = i
#
# print('\nСамый маленький доход у {}. Он составляет {} рублей'.format(name, val))
#
# incomes.pop(name)
# print('\nИтоговый словарь: ', incomes)



# Задача 3. Гистограмма частоты

# text = input('Введите текст: ')
# dct = dict()
#
# for i in text:
#     if i in dct:
#         dct[i] += 1
#     else:
#         dct[i] = 1
#
# for i in sorted(dct):
#     print(i, ':', dct[i])
#
# print('Максимальная частота:', max(dct.values()))



# 19.3 Вложенные словари и значения по умолчанию в get

# Задача 1. Член семьи

# family_member = {
#
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [ {"name": "Alice", "age": 6 },{"name": "Bob","age": 8} ]
#
#                 }
#
# print('Имя', family_member['name'])
# print('Фамилия', family_member['surname'])
# print('Хобби ', end = '')
# lst = family_member['hobbies']
# print(' '.join(lst))
# print(family_member['age'])
# print(family_member['children'][0]['name'], family_member['children'][0]['age'])
# print(family_member['children'][1]['name'], family_member['children'][1]['age'])
#
# n = input('Введите имя: ')
# for i in family_member['children']:
#     if i['name'] == n:
#         print(n)
#     else:
#         print('Нет такого имени')

# Задача 2. Игроки
#
# players_dict = {
#
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
#
# }
#
# print('Все члены команды из команды А, которые отдыхают')
# a = [i['name'] for i in players_dict.values() if i['status'] == 'Rest' and i['team'] == 'A']
# # for i in players_dict.values():
# #     if i['status'] == 'Rest' and i['team'] == 'A':
# #         print(i['name'])
#
# print(' '.join(a))


# 19.4 Множества. Функция set

# Задача 1. Пунктуация

# sym = {'!', '.', ',', '?', ';', ':'}
# count = 0
# text = input('Введите строку: ')
#
# for i in text:
#     if i in sym:
#         count += 1
# print('Количество знаков пунктуации:', count)


# Задача 2. Семинар

# import random
# nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
#
# nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
#
# nums_1 = set(nums_1)
# nums_2 = set(nums_2)
#
# print('1-е множество:', nums_1)
# print('2-е множество:', nums_2)
#
# print('\nМинимальный элемент 1-го множества:', min(nums_1))
# print('Минимальный элемент 2-го множества:', min(nums_2))
#
# nums_1.remove(min(nums_1))
# nums_2.remove(min(nums_2))
# a = (random.randint(100, 200))
# b = (random.randint(100, 200))
# nums_1.add(a)
# nums_2.add(b)
#
# print('\nСлучайное число для 1-го множества:', a)
# print('Случайное число для 2-го множества:', b)
#
# print('\nОбъединение множеств:', set(nums_1 | nums_2))
# print('\nПересечение множеств:', set(nums_1 & nums_2))
# print(nums_1)
# print(nums_2)
#
# print('\nЭлементы, входящие в nums_2, но не входящие в nums_1:', nums_2 - nums_1)


# Задача 3. Различные цифры
#
# n = input('Введите строку: ')
# print(n)
# result = ''
#
# for i in n:
#     if i.isdigit():
#         result += i
#
# print(sorted(set(result)))



