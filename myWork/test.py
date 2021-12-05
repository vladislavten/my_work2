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

def foo1(start):
    if start == 0:
        return

    print(start)
    (foo1(start - 1))


foo1(100)