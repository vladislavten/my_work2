# Задача 1. Меню ресторана
#
# print('Доступное меню: ', end = '')
# menu = input().split(';')
# menuToday = ', '.join(menu)
# print('На данный момент в меню есть: ', menuToday)



# Задача 2. Самое длинное слово

# word = input('Введите слова через пробел: ').split()
#
# result = max((word), key = len)
# print('Самое длинное слово: ', result)
# print('Количество символов в слове: ', len(result))



# Задача 3. Файлы

# file_name = input('Название файла: ')
# sym = '@', '№', '$', '%', '^', '&', '*', '(', ')'
#
#
# if file_name.startswith(sym):
#     print('\nОшибка: название начинается на один из специальных символов')
# elif file_name.endswith('.txt') or file_name.endswith('.docx'):
#     print('\nФайл назван верно.')
# else:
#     print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx')


# Задача 4. Заглавные буквы

# words = input('Введите строку: ').title()
# print('Результат: ', words)


# Задача 5. Пароль
#
# while True:
#     digit_count = 0
#     word_count = 0
#     word_up_count =0
#     password = input('Придумайте пароль: ')
#     for i_digit in password:
#         if i_digit.isdigit():
#             digit_count += 1
#
#     for i_word in password:
#         if i_word.isalpha():
#             word_count += 1
#
#     for i_word_upper in password:
#         if i_word_upper.isupper():
#             word_up_count += 1
#
#     if len(password) >= 8 and digit_count >= 3 and word_count >= 5 and word_up_count >= 1:
#         print('Это надёжный пароль!')
#         break
#     else:
#         print('Не надёжный пароль, попробуйте ещё раз')


# Задача 6. Сжатие

# s = input('Введите строку: ')
# count = 0
# result = ''
#
# for i in range(len(s)):
#     count += 1
#     if i == len(s) - 1:
#         result = result + s[i] + str(count)
#         break
#     if s[i] != s[i+1]:
#         result = result + s[i] + str(count)
#         count = 0
#
# print('Сжатый вариант: ', result)



# Задача 7. IP-адрес 2

# ip = input('Введите IP: ').split('.')
# flg = True
#
# for i in ip:
#     if not i.isdigit() and flg:
#         print(i, 'не целое число')
#         flg = False
#         break
#     elif int(i) > 255:
#         print(i, 'превышает 255')
#         flg = False
#         break
#     elif len(ip) != 4:
#         print('Адрес - это четыре числа, разделённые точками')
#         flg = False
#         break
#
# if flg == True:
#     print('Корректный IP адрес')



# Задача 8. Бегущая строка

# first_str = list(input('Первая строка: '))
# second_str = list(input('Вторая строчка строка: '))
# result = []
#
# count = -1
# flg = True
# for i in first_str:
#     if flg == False:
#         break
#     for x in second_str:
#         count += 1
#         if i == x:
#             flg = False
#             break
#
# for y in range(len(first_str)):
#     result.append(first_str[y - count])
#
# if result == second_str:
#     print('\nПервая строка получается из второй со сдвигом', count)
# else:
#     print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')


# Задача 9. Сообщение
#
# message = input('Сообщение ')
# word = ''
# out = ''
# for i in message:
#     if i.isalpha():
#         word += i
#     elif not i.isalpha():
#         word = word[::-1]
#         out += word
#         out += i
#         word = ''
# if len(word) >= 1:
#     print(word[::-1])
# else:
#     print(out)