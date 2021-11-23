# Задача 1. Песни 2

# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# }
# num = int(input('Сколько песен выбрать? '))
# all_time = 0
#
# for i in range(num):
#     song = input('Название {} песни: '.format(i + 1))
#     if song in violator_songs:
#         all_time += violator_songs[song]
#     else:
#         print('Такой песни нет')
#
# print('\nОбщее время звучания песен:', all_time, 'минут')



# Задача 2. География

a = input('Ввод: ')

b = a.split()
c = 'Новгород'
dct = dict()

dct[b[0]] = [b[1], b[2], b[3]]

for i in dct:
    for x in dct[i]:
        if x == c:
            print('Город {} расположен в стране {}.'.format(x, i))