# Задача 1. Challenge 2 (сделана)

def count(start):
    if start == 1:
        return start
    print(count(start - 1))
    return start

num = int(input('Введите число: '))
count(num + 1)
#

# Задача 2. Свой zip 2 (допилить осталось)

# def my_zip(*arg):
#     arg = list(map(list, arg))
#     try:
#         yield tuple(map(lambda x : x.pop(0), arg))
#         yield from my_zip(*arg)
#     except:
#         pass
#
# first_cort = (1, 2, 3)
# second_cort = (11, 22, 33, 44)
#
# print(*my_zip(first_cort, second_cort))



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


# Задача 5. Ускоряем работу функции (доделать)

# def calculating_math_func(data):
#     if data in factorials:
#         result = factorials[data]
#     else:
#         result = 1
#         for index in range(1, data + 1):
#             result *= index
#         factorials[data] = result
#     result /= data ** 3
#     result = result ** 10
#     return result
#
# factorials = {}
# print(calculating_math_func(5))
# print(factorials)



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

############################################################################
#
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



# Задача 7. Продвинутая функция sum (сделана)

# def summ(*args):
#     return sum(summ(*a) if isinstance(a, list) else a for a in args)
#
# print(summ(1, 2, 8, 4, 9))
# print(summ([[1, 2, [3]], [4], 5]))



# Задача 8. Список списков 2 (сделана)


def summ(nice_list, result = []):
    for i in nice_list:
        if isinstance(i, list):
            summ(i)
        else:
            result.append(i)
    return result


nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
print(summ(nice_list))


#
