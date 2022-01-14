# 24.2 Классы

# Задача 2. Однотипные объекты
# class Monitor:
#     name = 'Samsung'
#     matrix = 'VA'
#     res = 'WQHD'
#     freq = 60
#
# monitor_2 = Monitor()
# monitor_2.freq = 144
# print(monitor_2.freq)
#
# monitor_3 = Monitor()
# monitor_3.freq = 70
# print(monitor_3.freq)
#
# monitor_4 = Monitor()
# monitor_4.freq = 60
# print(monitor_4.freq)




# 24.3 Методы класса, аргумент self
#
# Задача 2. Семья

# class Family:
#     surname = 'Common family'
#     money = 100000
#     have_a_house = False
#
#     def info(self):
#         print(
#             'Family name: {} \nFamily funds: {}\nHaving a house: {}\n'.format(
#             self.surname, self.money, self.have_a_house
#             )
#         )
#     def earn_money(self, amount):
#         self.money += amount
#         print('Заработал {} денег! Денег в настоящий момент {}'.format(amount, self.money))
#
#     def buy_house(self, house_price, discount = 0):
#         house_price -= house_price * discount / 100
#         if self.money >= house_price:
#             self.money -= house_price
#             self.have_a_house = True
#             print('Дом куплен! Остаток денег: {}'.format(self.money))
#         else:
#             print('Не хватает денег')
#
# my_family = Family()
# my_family.info()
#
# print('Попытка купить дом\n')
# my_family.buy_house(10 ** 6)
#
# my_family.info()
# if not my_family.have_a_house:
#     my_family.earn_money(800000)
#     print('Очередная попытка купить дом')
#     my_family.buy_house(10 ** 6, 10)
#
# my_family.info()




# 24.4 Конструктор __init__ и работа с несколькими классами








# Задача 3. Весёлая ферма


# class Potato:
#
#
#
#
# class PotatoGarden:











