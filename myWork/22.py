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

# 22.3 Базовые операции с файлами: open, close, read


# import os
#
# file = open(os.path.abspath(os.path.join(os.path.sep, 'task', 'group_1.txt')), 'r', encoding='utf-8')
#
# summa = 0
# diff = 0
#
# lst = []
# for i_line in file:
#     info = i_line.split()
#     summa += int(info[2])
#     diff -= int(info[2])
#
#
# file_2 = open(os.path.abspath(os.path.join(os.path.sep, 'task', 'group_2.txt')), 'r', encoding='utf-8')
# for i_line in file_2:
#     info = i_line.split()
#     lst.append(int(info[2]))
# file.close()
# file_2.close()
# compose = lst[0] * lst[1] * lst[2]
# print(summa)
# print(diff)
# print(compose)



# 22.4 Метод write. Режимы записи

# Задача 1. Сумма чисел

# import os
#
# file = open(os.path.abspath(os.path.join(os.path.sep, 'task', 'numbers.txt')), 'r', encoding='utf-8')
# print('Содержимое файла: numbers.txt')
# summ = 0
# for i_int in file:
#     print(i_int, end = '')
#     summ += int(i_int)
#
# print()
# answer = open(os.path.abspath(os.path.join(os.path.sep, 'task', 'answer.txt')), 'w')
# answer.write(str(summ))
# answer.close()
# answer = open(os.path.abspath(os.path.join(os.path.sep, 'task', 'answer.txt')), 'r')
# print()
# print('Содержимое файла answer.txt по пути:', os.path.abspath(os.path.join(os.path.sep, 'task', 'answer.txt')))
# for i_int in answer:
#     print(i_int, end = '')



# Задача 2. Всё в одном

import os

def find(path, name):
    for i_elem in os.listdir(path):
        if os.path.isdir(os.path.join(path, i_elem)):
            find(os.path.join(path, i_elem), name)
        if os.path.isfile(os.path.join(path, i_elem, name)):
            open_file = open(os.path.abspath(os.path.join(os.path.sep, 'task', 'scripts.txt')), 'a')
            source_file = open(os.path.join(path, i_elem, name), 'r', encoding='utf-8')
            for i in source_file:
                open_file.write(i)
            open_file.write('\n')
            open_file.write('*' * 40)
            open_file.write('\n')

abs_path = 'D:\Python_Basic'
true_path = os.path.abspath(abs_path)
file_name = 'main.py'

find(true_path, file_name)