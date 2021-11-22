
# 19.1 Словарь: основы

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

# info = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ').split()
#
# dct = dict()
#
# dct['Имя'] = info[0]
# dct['Фамилия'] = info[1]
# dct['Город'] = info[2]
# dct['Место учёбы'] = info[3]
# dct['Оценки'] = []
#
# for i in info[4:]:
#     dct['Оценки'].append(i)
#
# for i in dct:
#     print(i, '-', dct[i])



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