films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favorite = []
enter_film = ''
print('Для завершения программы введите "end"')
while enter_film != 'end':
    enter_film = input('Введите фильм: ')
    flg = False
    for i in films:
        if enter_film == i:
            flg = True
    if flg == True:
        print('Фильм добавлен в список любимых фильмов')
        favorite.append(enter_film)
    else:
        print('Ошибка. Такого фильма нет')

print('Cписок любимых фильмов: ', favorite)
