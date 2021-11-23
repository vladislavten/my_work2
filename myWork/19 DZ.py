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
# 1 страна: Россия Москва Петербург Новгород
#
# 2 страна: Германия Берлин Лейпциг Мюнхен
nums_country = int(input('Количество стран: '))
dct = dict()

for i in range(1, nums_country + 1):
    country = input('{} страна: '.format(i)).split()
    dct[country[0]] = {country[1], country[2], country[3]}

for number in range(1, 4):
    city = input('\n{} город: '.format(number))
    for i in dct:
        if city in dct[i]:
            print('Город {} расположен в стране {}.'.format(city, i))
        else:
            print('По городу {} данных нет.'.format(city))


