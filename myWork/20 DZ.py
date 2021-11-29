
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

# text = 'О Дивный Новый мир!'
# text = ('й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к')
# text = [100, 200, 300, 'буква', 0, 2, 'а']
text = {22: 'д', 1: 'а', 23: 'а', 3: 'в', 89: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}
# result = [text[index] for index, values in enumerate(text) if index % 2 == 0]

result = [text[index] for index in range(1, len(text), 2)]


# result = [text[i] for i in range(0, len(text), 2)]
print(result)