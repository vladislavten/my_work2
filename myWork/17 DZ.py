
# Задача 1. Гласные буквы
# vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
#
# text = input('Введите текст: ')
# result = [letter for letter in text
#                       for x in vowels
#                           if letter == x]
#
# print('Список гласных букв: ', result)
# print('Длина списка:', len(result))



# Задача 2. Генерация

# import random
# N = int(input('Введите число: '))
#
# lst_N = [random.randint(1, 100) for _ in range(N)]
# lst_N = [1 if i % 2 == 0 else i % 5 for i in range(0, len(lst_N))]
#
# print('Результат:', lst_N)



# Задача 3. Случайные соревнования

# import random
# first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
# second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
#
# result = [first_team[i] if first_team[i] > second_team[i] else second_team[i] for i in range(20)]
#
# print('Первая команда:', first_team)
# print('\nВторая команда:', second_team)
# print('\nПобедители тура:', result)



# Задача 4. Тренируемся со срезами

# alphabet = 'abcdefg'
# copy_alphahet = alphabet[:]
# print(copy_alphahet)
# print(alphabet[::-1])
# print(alphabet[::2])
# print(alphabet[1::2])
# print(alphabet[:1])
# print(alphabet[6:5:-1])
# print(alphabet[3:4])
# print(alphabet[4:])
# print(alphabet[3:5])
# print(alphabet[4:2:-1])


# Задача 5. Разворот

# string = input('Введите слово с двумя "h": ')
# first = string.index('h')
# last = string.rindex('h')
# print('Результат:', (string[first + 1:last])[::-1])


# Задача 6. Сжатие списка

# N = [2, 3, 0, 4, 0, 4, 0, 3, 56, 0, 2, 0, 34, 0, 3]
#
# result = [i for i in N if i > 0]
# zeros = [i for i in N if i == 0]
# result.extend(zeros)
# print(result)



# Задача 7. Двумерный список

# import random
# def generate():
#     lst = [random.randint(1, 15) for _ in range(3)]
#     return lst
#
# result = [generate() for _ in range(4)]
#
# print('Результат:', result)

# Задача 8. Развлечение
#
# sticks = int(input('Кол-во палок: '))
# throws = int(input('Кол-во бросков: '))
#
# lst = ['|' for i in range(sticks)]
#
# for i in range(1, throws + 1):
#     print('Бросок', i, '. ', end = '')
#     print('Сбиты палки с номера', end = '')
#     a = int(input(' '))
#     print('по номер', end = '')
#     b = int(input(' '))
#     for z in range (a - 1, b):
#         lst[z] = '.'
#
# for i in lst:
#     print(i, end = '')

# Задача 9. Список списков

# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# result = [nice_list[i][x][y] for i in range(len(nice_list)) for x in range(3) for y in range(3)]
#
# print('Ответ:', result)



# Задача 10. Шифр Цезаря (сделайте по желанию)