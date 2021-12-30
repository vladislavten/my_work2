# TODO здесь писать код
import os
#
# text = input('Введите строку: ')
# save_path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split(' ')
# file_name = input('Введите имя файла: ')

text = 'testiruyem'
save_path = 'Python_Basic Module22'.split(' ')
file_name = 'my_document'
format_file = '.txt'

rel_path = os.path.sep.join(save_path)

print(os.path.abspath(os.path.join(os.path.sep, rel_path, file_name + '.txt')))

file = open('os.path.abspath(os.path.join(os.path.sep, rel_path, file_name + format_file', 'w')

print(os.path.abspath(os.path.join(os.path.sep, rel_path, file_name + format_file)))