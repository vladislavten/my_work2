# 21.2 Рекурсия
# Задача 1. Challenge

# def factorial(num):
#     if num == 1:
#         return 1
#     fac = num * factorial(num - 1)
#     return fac
#
# result = factorial(5)
#
# print(result)


# Задача 2. Степень числа

# def power(a, n):
#     if n == 0:
#         return 1
#     else:
#         return a * power(a, n - 1)
#
#
# float_num = float(input('Введите вещественное число: '))
#
# int_num = int(input('Введите степень числа: '))
#
# print(float_num, '**', int_num, '=', power(float_num, int_num))

# Задача 3. Поиск элемента

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(struct, key):
    if key in struct:
        return struct[key]
    for i in struct.values():
        if isinstance(i, dict):
            result = find_key(i, key)
            if result:
                break
    else:
        result = None

    return result

find = input('Какой ключ ищем? ')
result = find_key(site, find)
if result:
    print(result)
else:
    print('Такого ключа в структуре сайта нет')


