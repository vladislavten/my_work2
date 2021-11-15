# МОДУЛЬ 17.2
# Задача 3. Повышение цен

# def percent(x, price):
#     result = price + (price / 100 * x)
#     return result
#
# nums = int(input('Введите кол-во товаров: '))
# prices = []
# for i_price in range(nums):
#     price = float(input('Введите цену: '))
#     prices.append(price)
#
# X = float(input('Введите повыщение за первый год: '))
# Y = float(input('Введите повыщение за второй год: '))
#
# result = sum([percent(X, i) for i in prices])
# result2 = sum([percent(Y, i) for i in prices])
# print(round(sum(prices), 2), round(result, 2) , round(result2, 2))

########################################################
# МОДУЛЬ 17.3
# Задача 1. Список чётных числ
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
#
# lst = [i for i in range(a, b + 1) if i % 2 == 0]
#
# print(lst)

############################################################
# Задача 2. Магазин

# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16, -12]
# result = [(new_price if new_price > 0 else 0) for new_price in original_prices]

# print(result)

##############################################################

# Задача 3. Отряды
# import random
#
# frst_sq = [random.randint(50, 80) for _ in range(10)]
# scnd_sq = [random.randint(30, 60) for _ in range(10)]
# trd_sq = ['Выжил' if frst_sq[i] + scnd_sq[i] < 100 else 'Погиб'
#           for i in range(10)]
#
# print('Урон первого отряда:', frst_sq)
# print('\nУрон второго отряда:', scnd_sq)
# print('Состояние третьего отряда:', trd_sq)

#############################################################

# МОДУЛЬ 17.4

nums = [x for x in range(1, 101) if x % 10 == 0]
print(nums)
new_nums = nums
new_nums[3] = 0
print(new_nums)

for i_elem in range(2, 8):
    print(new_nums[i_elem], end = ' ')



# ТАЙМЕР
# import time
# start_time = time.time()
# a = []
# for i in range(10000000):
#     i *= 2
#     a.append(i)
#
# a = [x * 2 for x in range(10000000)]
# print(a)
# print("--- %s seconds ---" % (time.time() - start_time))


