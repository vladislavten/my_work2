# Задача 1. Песни 2

# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# }
# num = int(input('Сколько песен выбрать? '))
# all_time = 0
#
# for i in range(num):
#     song = input('Название {} песни: '.format(i + 1))
#     if violator_songs.get(song):
#         all_time += violator_songs[song]
#     else:
#         print('Такой песни нет')
#
# print('\nОбщее время звучания песен:', all_time, 'минут')



# Задача 2. География

#
# 1 страна: Россия Москва Петербург Новгород
#
# 2 страна: Германия Берлин Лейпциг Мюнхен
#
# dct = {}
# nums_country = int(input('Кол-во стран: '))
# for i in range(0, nums_country):
#     value = input(f'{i + 1} страна: ').split()
#     for town in value[1:]:
#         dct[town] = value[0]
# print(dct)
#
# for i in range(1, 4):
#     city = input(f'{i} город: ')
#     country = dct.get(city)
#     if country:
#         print(f'Город {city} расположен в стране {country}.')
#     else:
#         print(f'По городу {city} данных нет.')



# Задача 3. Криптовалюта
# data = {
#
#     "address": "0x544444444444",
#
#     "ETH": {
#         "balance": 444,
#         "totalIn": 444,
#         "totalOut": 4
#             },
#
#     "count_txs": 2,
#
#     "tokens": [
#
#         {
#
#             "fst_token_info": {
#
#                 "address": "0x44444",
#
#                 "name": "fdf",
#
#                 "decimals": 0,
#
#                 "symbol": "dsfdsf",
#
#                 "total_supply": "3228562189",
#
#                 "owner": "0x44444",
#
#                 "last_updated": 1519022607901,
#
#                 "issuances_count": 0,
#
#                 "holders_count": 137528,
#
#                 "price": False
#
#             },
#
#             "balance": 5000,
#
#             "totalIn": 0,
#
#             "total_out": 0
#
#         },
#
#         {
#
#             "sec_token_info": {
#
#                 "address": "0x44444",
#
#                 "name": "ggg",
#
#                 "decimals": "2",
#
#                 "symbol": "fff",
#
#                 "total_supply": "250000000000",
#
#                 "owner": "0x44444",
#
#                 "last_updated": 1520452201,
#
#                 "issuances_count": 0,
#
#                 "holders_count": 20707,
#
#                 "price": False
#
#             },
#
#             "balance": 500,
#
#             "totalIn": 0,
#
#             "total_out": 0
#
#         }
#
#     ]
#
# }
#
# for i in data:
#     print(i, '-', data[i])
# print()
#
# data['ETH'].update({'total_diff' : 100})
# data['tokens'][0]['fst_token_info'].update({'name' : 'doge'})
# data['ETH']['total_out'] = data['tokens'][0].pop('total_out')
# data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')
#
# print('Результат манипуляций')
# for i in data:
#     print(i, '-', data[i])
# print()



# Задача 4. Товары

# goods = {
#
#     'Лампа': '12345',
#
#     'Стол': '23456',
#
#     'Диван': '34567',
#
#     'Стул': '45678',
#
# }
#
# store = {
#
#     '12345': [
#
#         {'quantity': 27, 'price': 42},
#
#     ],
#
#     '23456': [
#
#         {'quantity': 22, 'price': 510},
#
#         {'quantity': 32, 'price': 520},
#
#     ],
#
#     '34567': [
#
#         {'quantity': 2, 'price': 1200},
#
#         {'quantity': 1, 'price': 1150},
#
#     ],
#
#     '45678': [
#
#         {'quantity': 50, 'price': 100},
#
#         {'quantity': 12, 'price': 95},
#
#         {'quantity': 43, 'price': 97},
#
#     ],
#
# }
#
# for i in goods:
#     summ = 0
#     quantity = 0
#     if goods[i] in store:
#         for y in range(len(store[goods[i]])):
#             summ += store[goods[i]][y]['quantity'] * store[goods[i]][y]['price']
#             quantity += store[goods[i]][y]['quantity']
#         print('{} - {} шт, стоимость {} руб'.format(i, quantity, summ))



# Задача 5. Гистограмма частоты 2

# text = input('Введите текст: ')
# dct = dict()
# dct_invert = dict()
# for i in text:
#     if i in dct:
#         dct[i] += 1
#     else:
#         dct[i] = 1

# for i in sorted(dct):
#     print(i, ':', dct[i])
#
#
# for i in dct:
#     if dct[i] in dct_invert:
#         dct_invert[dct[i]].append(i)
#     else:
#         dct_invert[dct[i]] = [i]
#
# print('\nИнвертированный словарь частот:')
#
# for i in dct_invert:
#     print(i, ':', dct_invert[i])



# Задача 6. Словарь синонимов

# dct = dict()
#
# for i in range(1, (int(input('Введите количество пар слов: '))) + 1):
#     pair = input('{} пара: '.format(i)).split(' - ')
#     dct[pair[0]] = pair[1]
#     dct[pair[1]] = pair[0]
#
# while True:
#     word = input('Введите слово: ')
#     if dct.get(word):
#         print('Синоним: ', dct[word])
#     else:
#         print('Такого слова в словаре нет.')


# Задача 7. Пицца


# n = int(input('Введите кол-во заказов: '))
# d = {}
# for i in range(1, n + 1):
#     order = input(f'{i} заказ: ').split()
#     fio, pizza, amount = order[0], order[1], int(order[2])
#
#     if fio not in d:
#         d[fio] = {pizza: amount}
#     else:
#         if pizza not in d[fio]:
#             d[fio] |= {pizza: amount}
#         else:
#             d[fio][pizza] += amount
# for fio, order in sorted(d.items()):
#     print(f'{fio}:')
#     for pizza, amount in sorted(order.items()):
#         print('\t', pizza, amount)


# Задача 8. Угадай число
#
# number = {str(i) for i in range(1, int(input('Введите максимальное число: ')) + 1)}
# while True:
#     choice = input('Нужное число есть среди вот этих чисел: ')
#     if choice == 'Помогите':
#         print('Артём мог загадать следующие числа:', sorted(number))
#         break
#     choice = choice.split(' ')
#     choice = set(choice)
#     answer = input('Ответ Артёма: ')
#     if answer == 'Да' or answer == 'да':
#         number = number & choice
#     elif answer == 'нет' or answer == 'Нет':
#         number = number - choice

# Задача 9. Родословная

# def height(man):
#     if man not in p_tree:
#         return 0
#     else:
#         return 1 + height(p_tree[man])
#
# p_tree = {}
# n = int(input('Введите количество человек: '))
# for i in range(n - 1):
#     child, parent = input(f'{i + 1} пара: ').split()
#     p_tree[child] = parent
#
# heights = {}
# for man in set(p_tree.keys()).union(set(p_tree.values())):
#     heights[man] = height(man)
# print('\n“Высота” каждого члена семьи:')
# for key, value in sorted(heights.items()):
#     print(key, value)

