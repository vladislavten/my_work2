# Задача 1. Challenge 2

# def count(start):
#     if start == 1:
#         return start
#     print(count(start - 1))
#     return start
#
# num = int(input('Введите число: '))
# count(num + 1)
#

# Задача 2. Свой zip 2



# Задача 3. Ряд Фибоначчи
#
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# n = int(input("Номер элемента ряда Фибоначчи: "))
# print('Значение этого элемента:', fibonacci(n))


# Задача 4. Поиск элемента 2

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



# Задача 6. Глубокое копирование   (ДОДЕЛАТЬ вывод "Сайт для ...")

# def func(num, name, site):
#     if num == 0:
#         return site
#
#     site['html']['head']['title'] = f'Куплю/продам телефон {name} недорого'
#     site['html']['body']['h2'] = f'У нас самая низкая цена на {name}'
#
#     print(func(num - 1, name, site))
#
#     return site
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
# name = input('Введите название продукта для нового сайта: ')
#
# func(site_num, name, site)

