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
# sym = '@№$%^&*()'
#
# for i_sym in sym:
#     if file_name.startswith(i_sym):
#         print('\nОшибка: название начинается на один из специальных символов')
#         break
#     if file_name.endswith('.txt') or file_name.endswith('.docx'):
#         print('\nФайл назван верно.')
#         break
#     else:
#         print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx')
#         break



# Задача 4. Заглавные буквы

# words = input('Введите строку: ').title()
# print('Результат: ', words)


# Задача 5. Пароль

while True:
    digit_count = 0
    word_count = 0
    word_up_count =0
    password = input('Придумайте пароль: ')
    for i_digit in password:
        if i_digit.isdigit():
            digit_count += 1

    for i_word in password:
        if i_word.isalpha():
            word_count += 1

    for i_word_upper in password:
        if i_word_upper.isupper():
            word_up_count += 1

    if len(password) >= 8 and digit_count >= 3 and word_count >= 5 and word_up_count >= 1:
        print('Это надёжный пароль!')
        break
    else:
        print('Не надёжный пароль, попробуйте ещё раз')

#
# Пример:
#
# Придумайте пароль: qwerty
#
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Это надёжный пароль!