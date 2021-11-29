
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
def i_prime(n):
    # lst = []
    #
    # for p in range(2, n):
    #     for i in range(2, p):
    #         if p % i == 0:
    #             break
    #     else:
    #         lst.append(p)
    # return lst
    return [p if p % i == 0 else p for p in range(2, n)
                                                for i in range(2, p)]

text = 'О Дивный Новый мир!'
# text = ('й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к')
# text = [100, 200, 300, 'буква', 0, 2, 'а']
# text = {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}
#
#
#
# result = [text[index] for index, values in enumerate(text) if index in lst]
# print(lst)
lst = i_prime(len(text))
result = [text[index] for index in lst]
#
print(result)


