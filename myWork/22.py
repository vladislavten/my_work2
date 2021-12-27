# 22.1 Модуль os: генерация путей и метод listdir

# Задача 1. Сисадмин
# import os
#
# folder = 'access'
# file_name = 'admin.bat'
#
# abs_path = os.path.abspath(os.path.join(folder, file_name))
# print(abs_path)
#
# rel_path = os.path.join(folder, file_name)
#
# print(rel_path)


# Задача 2. Содержимое

# import os
#
# path = 'C:\Python310'
#
# for i_elem in os.listdir(path):
#     print(os.path.join(path, i_elem))
#
# print(os.path.abspath(os.path.join(os.path.sep,'123') )) #пример работы os.path......


# Задача 3. Корень диска

# import os
#
# print('Корень диска:', os.path.abspath(os.path.sep))




# 22.2 Модуль os: проверки

# Задача 1. Иконки

# import os
#
# file = 'C:\Python_Basic'
# true_path = os.path.abspath(file)
# print('Путь:', true_path)
# result = 0
# if os.path.isfile(true_path):
#     print('Это файл')
#     print('Размер файла:', os.path.getsize(true_path), 'байт')
# elif os.path.isdir(true_path):
#     for i_elem in os.listdir(true_path):
#         print(os.path.join(true_path, i_elem))
#         result += os.path.getsize(true_path)
#         print(result)
#     print('Это папка')
#     print('Размер папки:', result, 'байт')
# else:
#     print('Указанного пути не существует')



# Задача 2. Поиск файла

# import os
#
# def find(path, name):
#     for i_elem in os.listdir(path):
#         if os.path.isdir(os.path.join(path, i_elem)):
#             find(os.path.join(path, i_elem), name)
#         if os.path.isfile(os.path.join(path, i_elem, name)):
#             print(os.path.join(path, i_elem, name))
#
# abs_path = 'C:\Python_Basic'
# true_path = os.path.abspath(abs_path)
# file_name = '111.txt'
#
# find(true_path, file_name)


import os

# print(os.path.abspath(os.path.join(os.path.sep, 'task', 'group_1.txt' )))

file = open(os.path.abspath(os.path.join(os.path.sep, 'task', 'group_1.txt')), 'r', encoding='utf-8')
# data = file.read()

summa = 0
for i_line in file:
    info = i_line.split()
    print(info)
    summa += int(info[2])

# file = open('E:\task\group_1.txt', 'read')
# diff = 0
#
# for i_line in file:
#     info = i_line.split()
#     diff -= info[2]
#
# file_2 = open('E:\task\group_2.txt', 'read')
# compose = 0
#
# for i_line in file:
#     info = i_line.split()
#     compose *= info[2]

print(summa)
# print(diff)
# print(compose)