# TODO здесь писать код
import os

def count_files(path, count = []): #Считаю количество файлов

    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            count.append(1)
        if os.path.isdir(os.path.join(path, i)):
            count_files(os.path.join(path, i))
    return count

def file_size(path, size = []): #Считаю размеры всех папок и файлов и записываю в список size
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            size.append(os.path.getsize(os.path.join(path, i)))
        if os.path.isdir(os.path.join(path, i)):
            file_size(os.path.join(path, i))
    return size

enter_path = input('Пожалуйста, введите путь до директории: ')

files = count_files(enter_path)

size = file_size(enter_path)
general_size = 0
for i_size in size:
    general_size += i_size

count = 0
for i_elem in os.listdir(enter_path):
    if os.path.isdir(os.path.join(enter_path, i_elem)):
        count += 1

print(general_size)
print('Размер каталога (в Кб):', round(general_size / 1024, 2))
print('Количество подкаталогов:', count)
print('Количество файлов: ', len(files))