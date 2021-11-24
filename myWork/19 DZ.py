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

#
# 1 страна: Россия Москва Петербург Новгород
#
# 2 страна: Германия Берлин Лейпциг Мюнхен
#
# dct = {}
# nums_country = int(input('Кол-во стран: '))
# for i in range(0, nums_country):
#     value = input(f'{i + 1} страна: ').split()
#     for town in value[1:]:
#         dct[town] = value[0]
#
# for i in range(1, 4):
#     city = input(f'{i} город: ')
#     country = dct.get(city)
#     if country:
#         print(f'Город {city} расположен в стране {country}.')
#     else:
#         print(f'По городу {city} данных нет.')



# Задача 3. Криптовалюта
data = {

    "address": "0x544444444444",

    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
            },

    "count_txs": 2,

    "tokens": [

        {

            "fst_token_info": {

                "address": "0x44444",

                "name": "fdf",

                "decimals": 0,

                "symbol": "dsfdsf",

                "total_supply": "3228562189",

                "owner": "0x44444",

                "last_updated": 1519022607901,

                "issuances_count": 0,

                "holders_count": 137528,

                "price": False

            },

            "balance": 5000,

            "totalIn": 0,

            "total_out": 0

        },

        {

            "sec_token_info": {

                "address": "0x44444",

                "name": "ggg",

                "decimals": "2",

                "symbol": "fff",

                "total_supply": "250000000000",

                "owner": "0x44444",

                "last_updated": 1520452201,

                "issuances_count": 0,

                "holders_count": 20707,

                "price": False

            },

            "balance": 500,

            "totalIn": 0,

            "total_out": 0

        }

    ]

}

for i in data:
    print(i, '-', data[i])
print()

data['ETH'].update({'total_diff' : 100})
data['tokens'][0]['fst_token_info'].update({'name' : 'doge'})
data['ETH']['total_out'] = data['tokens'][0].pop('total_out')
data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')

print('Результат манипуляций')
for i in data:
    print(i, '-', data[i])
print()

