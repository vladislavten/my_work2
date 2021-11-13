# Задача 3. Повышение цен МОДУЛЬ 17.2

# def percent(x, price):
#     result = price + (price / 100 * x)
#     return result
#
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
import time
start_time = time.time()
# a = []
# for i in range(10000000):
#     i *= 2
#     a.append(i)

a = [x * 2 for x in range(10000000)]
print(a)
print("--- %s seconds ---" % (time.time() - start_time))


