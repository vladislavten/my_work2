
# Задача 1. Ревью кода
#
# students = {
#
#     1: {
#
#         'name': 'Bob',
#         'surname': 'Vazovski',
#         'age': 23,
#         'interests': ['biology', 'swimming']
#          },
#
#     2: {
#         'name': 'Rob',
#         'surname': 'Stepanov',
#         'age': 24,
#         'interests': ['math', 'computer games', 'running']
#
#     },
#
#     3: {
#         'name': 'Alexander',
#         'surname': 'Krug',
#         'age': 22,
#         'interests': ['languages', 'health food']
#
#     }
#
# }
#
# def f(dict):
#     lst = []
#     string = []
#     for index, value in dict.items():
#         lst.extend(value['interests'])
#         string.extend(value['surname'])
#     string = len(string)
#     return lst, string
#
#
# for i, value in students.items():
#     print('ID студента', i, '— возраст', value['age'])
#
#
# hobbies, ages = f(students)
# print('Список интересов:', ' '.join(hobbies))
# print('Общая длина всех фамилий:', ages)


# Задача 2. Универсальная программа 2
#
# def i_prime(n):
#     n = len(n)
#     lst = []
#
#     for p in range(2, n):
#         for i in range(2, p):
#             if p % i == 0:
#                 break
#         else:
#             lst.append(p)
#     return lst
#
# ######### переменные на выбор:
# text = 'О Дивный Новый мир!'
# # text = ('й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к')
# # text = [100, 200, 300, 'буква', 0, 2, 'а']
# # text = {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}
# ################################
# lst = i_prime(text)
# result = [text[index] for index in lst]
#
# print(result)


# Задача 3. Функция

# def func(cort, elem):
#     new_cort = []
#     index =[]
#
#     for i, y in enumerate(cort):
#         if y == elem:
#             index.append(i)
#     if len(index) >= 2:
#         new_cort.extend(cort[index[0]:index[1]+1])
#     elif len(index) == 1:
#         new_cort.extend(cort[index[0]:])
#
#     return tuple(new_cort)
#
# cort= ('с', 'а', 'й', 'г', 'а', '4', 'т', 'ж', 'н', 'Й')
#
# print('Дан кортеж: ', cort)
# elem = input('Введите элемент: ')
#
# print('\n', func(cort, elem))


# Задача 4. Игроки

# players = {
#     ("Ivan", "Volkin"): (10, 5, 13),
#     ("Bob", "Robbin"): (7, 5, 14),
#     ("Rob", "Bobbin"): (12, 8, 2)
# }
#
# lst = []
#
# for key, value in players.items():
#     lst.append(key + value)
#
# print(lst)


# Задача 5. Одна семья

family = {
    ("Сидоров", "Никита"): 35,
    ("Сидорова", "Алина"): 34,
    ("Сидоров", "Павел"): 10,
    ("Веселов", "Евгений"): 32,
    ("Веселова", "Виктория"): 29,
    ("Веселов", "Роман"): 5,

}
surname = input('Введите фамилию: ')
if surname[-1:] == 'а':
    surname2 = surname[:-1]
else:
    surname2 = surname + 'а'

for i, v in family.items():
    if surname in i:
        print(' '.join(i), v)
    elif surname2 in i:
        print(' '.join(i), v)
