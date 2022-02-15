import os


def gen_files_path() -> str:

    for dirs, folder, files in os.walk(os.path.abspath(os.sep)):
        for i_folder in folder:
            yield i_folder, dirs


find = input('Введите имя папки для поиска: ')

for find_folder, y_dir in gen_files_path():
    if find_folder == find:
        print('Искомая папка : ', find_folder)
        print('Находится по пути  ', y_dir)


