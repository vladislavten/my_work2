# TODO здесь писать код
dct = {}
nums_country = int(input('Кол-во стран: '))
for i in range(0, nums_country):
    value = input(f'{i + 1} страна: ').split()
    for town in value[1:]:
        dct[town] = value[0]
print(dct)

for i in range(1, 4):
    city = input(f'{i} город: ')
    country = dct.get(city)
    if country:
        print(f'Город {city} расположен в стране {country}.')
    else:
        print(f'По городу {city} данных нет.')