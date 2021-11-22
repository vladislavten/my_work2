# TODO здесь писать код
file_name = input('Название файла: ')
sym = '@', '№', '$', '%', '^', '&', '*', '(', ')'


if file_name.startswith(sym):
    print('\nОшибка: название начинается на один из специальных символов')
elif file_name.endswith('.txt') or file_name.endswith('.docx'):
    print('\nФайл назван верно.')
else:
    print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx')

