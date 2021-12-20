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


# Задача 7. Продвинутая функция sum

# def summ(*args):
#     return sum(summ(*a) if isinstance(a, list) else a for a in args)
#
# print(summ(1, 2, 8, 4, 9))
# print(summ([[1, 2, [3]], [4], 5]))



# Задача 8. Список списков 2


# def summ(args):
#     # return [num for row in listik for row_i in row for num in row_i]
#     return [summ(a) if isinstance(a, list) else a for a in args]

def summ(nice_list, result = []):
    for i in nice_list:
        if isinstance(i, list):
            summ(i)
        else:
            result.append(i)
    return result


nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
print(summ(nice_list))





