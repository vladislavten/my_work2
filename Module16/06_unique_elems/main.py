# TODO здесь писать код

first_list = []
second_list = []

print('Первый 3 числа')
for i in range(3):
    print('Введите', i + 1, 'число:', end = ' ')
    first = input()
    first_list.append(first)

print('\nВторые 7 чисел')
for i in range(7):
    print('Введите', i + 1, 'число:', end=' ')
    first = input()
    second_list.append(first)

first_list.extend(second_list)
first_list = list(set(first_list))

print('Новый первый список с уникальными элементами:', first_list)