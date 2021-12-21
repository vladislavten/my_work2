# Задача 1. Challenge 2 (сделана)

# def count(start):
#     if start == 1:
#         return start
#     print(count(start - 1))
#     return start
#
# num = int(input('Введите число: '))
# count(num + 1)
#

# Задача 2. Свой zip 2 (допилить осталось)

# def shortest_seq_range(string, tpl):
#     return min(len(string), len(tpl))
#
#
# syms_str = 'abcd'
# nums_tpl = (10, 20, 30, 40)
#
# pairs = ((syms_str[i_elem], nums_tpl[i_elem])
#          for i_elem in range(shortest_seq_range(syms_str, nums_tpl)))
#
# for i_elem in pairs:
#     print(i_elem)



# Задача 3. Ряд Фибоначчи (сделана)
#
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# n = int(input("Номер элемента ряда Фибоначчи: "))
# print('Значение этого элемента:', fibonacci(n))


# Задача 4. Поиск элемента 2 (сделана)

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
# def find_key(struct, key, deep):
#     if deep == 0:
#         return
#     if key in struct:
#         return struct[key]
#     for i in struct.values():
#         if isinstance(i, dict):
#             result = find_key(i, key,deep - 1)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
# find = input('Какой ключ ищем? ')
# deep = int(input('Введите глубину: '))
# result = find_key(site, find, deep)
# if result:
#     print(result)
# else:
#     print('Такого ключа в структуре сайта нет')


# Задача 5. Ускоряем работу функции

# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result




# Задача 6. Глубокое копирование   (сделана)

# import copy
#
# def func(num, site):
#     if num > 0:
#         name = input('Введите название продукта для нового сайта: ')
#         print(f'Сайт для {name}:')
#         site_copy = copy.deepcopy(site)
#         site_copy['html']['head']['title'] = f'Куплю/продам телефон {name} недорого'
#         site_copy['html']['body']['h2'] = f'У нас самая низкая цена на {name}'
#         print(site_copy)
#         func(num - 1, site_copy)
#
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
# site_num = int(input('Сколько сайтов: '))
#
# func(site_num, site)


# Задача 7. Продвинутая функция sum (сделана)

# def summ(*args):
#     return sum(summ(*a) if isinstance(a, list) else a for a in args)
#
# print(summ(1, 2, 8, 4, 9))
# print(summ([[1, 2, [3]], [4], 5]))



# Задача 8. Список списков 2 (сделана)


# def summ(nice_list, result = []):
#     for i in nice_list:
#         if isinstance(i, list):
#             summ(i)
#         else:
#             result.append(i)
#     return result
#
#
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# print(summ(nice_list))
#
#
#
