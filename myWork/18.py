# МОДУЛЬ 18.2 Форматирование строк: format и f-strings
#
# name = input('Введите имя: ')
# order = input('Введите номер заказа: ')
#
# print('Здравствуйте, {name}! Ваш номер заказа: {order}. Приятного дня!'.format(
#             name = name,
#             order = order
# ))


# Задача 2. Долги

# name = input('Введите имя: ')
# dolg = input('Введите долг: ')
#
# print('{name}! {name}, привет! Как дела, {name}? Где мои {dolg} рублей? {name}! '.format(
#             name = name,
#             dolg = dolg
# ))

#########################################################

# 18.3 Методы строк: split и join

# Задача 1. Улучшенная лингвистика 2

# words = input('Введите три слова через пробел: ').split()
# print(words)
#
# text = input('Введите текст: ').split()
#
# result = [i for i in text for x in words if i == x]
# print(len(result))


# Задача 2. Бабушка

# text = input('Введите текст: ').split()
# print('Исправленный текст: ', end = '')
# for i in text:
#     print(i, end = ' ')


# Задача 3. Разделители символов
#С днём рождения, {name}! С {age}-летием тебя!
# Список людей через запятую: Иван Иванов, Петя Петров, Лена Ленова
#
# Возраст людей через пробел: 20 30 18

# template = input('Введите шаблон поздравления, использую {name} и {age}: ')
# name = input('Введите имена и фамилии через запятую: ').split(', ')
# age = input('Введите возраст каждого человека (в одну строку через пробел): ').split()
#
# for i in range(len(name)):
#     print(template.format(name = name[i], age = age[i]))
#
# peoples = [' '.join([name[i], str(age[i])]) for i in range(len(name))]
#
# peoples_str = ', '.join(peoples)
# print('Именинники: ', peoples_str)

##################################################################################

# 18.4 Методы строк: startswith, endswith, upper, lower

# Задача 2. Путь к файлу


# path = 'C:/user/docs/folder/new_file.txt'
# print('Путь к файлу:', path)
#
# print('На каком диске должен лежать файл:', end = ' ')
# disk = input()
#
# print('Требуемое расширение файла:', end = ' ')
# format_file = input()
#
# if path.startswith(disk) and path.endswith(format_file):
#     print('Путь корректен!')
# else:
#     print('Путь не корректен')
#################################################################

# Задача 3. Удаление части

a = 'ЭтО ПИтон, ОН очеНь УдоБЫй КАК ВСЕГДА'
a = 'ПиТоН - ЭтО УДоБнО'

lower = [i for i in a if i.islower()]
upper = [i for i in a if i.is ()]

if len(lower) > len(upper):
    print(a.lower())
else:
    print(a.upper())




