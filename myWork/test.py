# def checking_array(checking_list):
#     return [i for i, v in enumerate(checking_list) if checking_num(i)]
#
# def checking_num(i_num):
#     k = 0
#     for i in range(2, i_num // 2 + 1):
#         if i_num % i == 0:
#             k = k + 1
#         if k <= 0:
#             return True
#         else:
#             return False
#
# # s = 'О Дивный Новый мир!'
# # text = 'О Дивный Новый мир!'
# # s = ('й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к')
# s = [100, 200, 300, 'буква', 0, 2, 'а']
# # s = {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}
#
# i_list = checking_array(s)
# print(i_list)
#
# for i in i_list:
#     print(s[i], end = ' ')


# Листинг 1
# вводим N
# n = int(input("n="))
# # создаем пустой список для хранения простых чисел
# lst = []
# # в k будем хранить количество делителей
# k = 0
# # пробегаем все числа от 2 до N
# for i in range(2, n+1):
#     # пробегаем все числа от 2 до текущего
#     for j in range(2, i):
#         # ищем количество делителей
#         if i % j == 0:
#             k = k + 1
#     # если делителей нет, добавляем число в список
#     if k == 0:
#         lst.append(i)
#     else:
#         k = 0
# # выводим на экран список
# print (lst)

# def test(a):
#     if a == 101:
#         return 1
#     print(a)
#     a += 1
#     test(a)
#
# a = 1
# test(a)

# def sort(nums):
#     for i in range(len(nums)):
#          for x in range(i, len(nums)):
#                if nums[x] < nums[i]:
#                      nums[x], nums[i] = nums[i], nums[x]

# def foo(start):
#     if start == 0:
#         return
#     print(foo(start - 1))
#     return start
#
#
# foo(100)
# print()
# print()

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


# Задача 2. Непонятно!


# import copy
#
# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам телефон недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на iphone',
#             'div': 'Купить',
#             'p': 'продать'
#         }
#     }
# }
#
#
# def func_all(site):
#     for _ in range(question):
#         product = input('Введите название продукта для нового сайта: ').lower()
#         print(f'Сайт для {product}:')
#         site_copy = copy.deepcopy(site)
#         site_copy['html']['head']['title'] = f'Куплю/продам {product} недорого'
#         site_copy['html']['body']['h2'] = f'У нас самая низкая цена на {product}'
#         func(site_copy)
#
#
# def func(s, depth=0):
#     for i in s:
#         print(' ' * depth, i)
#         if isinstance(s[i], dict):
#             func(s[i], depth + 1)
#         else:
#             print(' ' * (depth + 1), ' '.join(s[i]))
#
#
# question = int(input('\nСколько будет сайтов: '))
# func_all(site)

# import copy
#
# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам телефон недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на iphone',
#             'div': 'Купить',
#             'p': 'продать'
#         }
#     }
# }
#
#
# def find_key(struct, key, meaning):
#     if key in struct:
#         struct[key] = meaning
#         return site
#
#     for sub_struct in struct.values():
#         if isinstance(sub_struct, dict):
#             result = find_key(sub_struct, key, meaning)
#             if result:
#                 return site
#
#
#
# number_sites = int(input('Сколько сайтов: '))
# site_copy = copy.deepcopy(site)
# for _ in range(number_sites):
#     product_name = input('Введите название продукта для нового сайта: ')
#     key = {'title': f'Куплю/продам {product_name} недорого', 'h2': f'У нас самая низкая цена на {product_name}'}
#     for i in key:
#         find_key(site_copy, i, key[i])
#
#     print(f'Сайт для {product_name}:')
#     print(site_copy, '\n')

# ПОКЕР###########################


from random import randint , choice

class Cards:
    cards = ['A',2,3,4,5,6,7,8,9,10,10,10,10]
    diller_card = [choice(cards),choice(cards)]
    def __init__(self, player):
        player.extend([choice(self.cards),choice(self.cards)])

    def one_card(self,cards):
        cards.extend([choice(self.cards)])

    def count(self,cards):
        result = 0
        A_player = []
        for i_card in cards:
            if isinstance(i_card, int):
                result += i_card
            elif isinstance(i_card, str):
                A_player.append(i_card)
        if A_player:
            for _ in A_player:
                if result < 11:
                    result += 11
                elif result >= 11:
                    result += 1
        return result

player_card = []
diller_card = []

player = Cards(player_card)
diller = Cards(diller_card)

player_flg = False
diller_flg = False

while True:
    if player.count(player_card) > 21:
        print('Карты игрока:', player_card)
        print('У вас перебор! Сумма очков:', player.count(player_card))
        print('Диллер победил')
        player_flg = True
        break

    print('Карты игрока:', player_card, 'обшая сумма очков:', player.count(player_card))

    player_choice = input('\nВыберите действие:\n1 = взять еще карту\n2 = Остановиться\nВвод: ')
    if player_choice == '1':
        player.one_card(player_card)
    elif player_choice == '2':

        while True:
            if diller.count(diller_card) > 21:
                diller_flg = True
                break
            if diller.count(diller_card) >= 17:
                break
            if diller.count(diller_card) < 17:
                diller.one_card(diller_card)

        print('Карты игрока:', player_card, 'обшая сумма очков:', player.count(player_card))
        print('Карты диллера:', diller_card, 'обшая сумма очков:', diller.count(diller_card))
        if diller_flg:
            print('Выиграл игрок!')
        elif player_flg:
            print('Выиграл диллер!')
        elif player.count(player_card) < diller.count(diller_card):
            print('Выиграл диллер!')
        elif player.count(player_card) > diller.count(diller_card):
            print('Выиграл игрок!')
        else:
            print('Ничья')
        break
    else:
        print('Ошибка ввода, выберите 1 или 2')

