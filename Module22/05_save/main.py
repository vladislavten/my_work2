# TODO здесь писать код
import os

def save_file(text):
    save_path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split(' ')
    file_name = input('Введите имя файла: ')
    format_file = '.txt'
    rel_path = os.path.sep.join(save_path)

    if os.path.exists(os.path.abspath(os.path.join(os.path.sep, rel_path))):
        if os.path.exists(os.path.abspath(os.path.join(os.path.sep, rel_path, file_name + format_file))):
            print('Вы действительно хотите перезаписать файл?', end= ' ')
            rewrite = input().lower()
            if rewrite == 'да':
                file = open(os.path.abspath(os.path.join(os.path.sep, rel_path, file_name + format_file)), 'w',
                            encoding='utf-8')
                file.write(text)
                print('Файл успешно перезаписан!')
            elif rewrite == 'нет':
                print('Файл не был перезаписан.')
            else:
                print('Введен не верный ответ, необходимо вводить "Да" или "Нет"')
        else:
            file = open(os.path.abspath(os.path.join(os.path.sep, rel_path, file_name + format_file)), 'w',
                        encoding='utf-8')
            file.write(text)
            print('Файл успешно сохранён!')
    else:
        print('Такого пути не существует')

text = input('Введите строку: ')

save_file(text)