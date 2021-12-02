# TODO здесь писать код

dct = dict()
for i in range(1, int(input('Сколько записей вносится в протокол? ')) + 1):
    enter_result = input(f'{i} запись: ').split()
    if not enter_result[1] in dct:
        dct[i] = int(enter_result[0]), enter_result[1]
    else:
        if int(enter_result[0]) > dct[enter_result[1]][0]:
            dct[i] = int(enter_result[0]), enter_result[1]

# dct = {1: (69485, 'Jack'),
#        2: (95715, 'qwerty'),
#        3: (95715, 'Alex'),
#        4: (83647, 'M'),
#        5: (197128, 'qwerty'),
#        6: (95715, 'Jack'),
#        7: (93289, 'Alex'),
#        8: (95715, 'Alex'),
#        9: (95715, 'M')
#        }
#
print('\nРезультаты: ')
for place in range(1, 3 + 1):
    a = [0, 0]
    for v in dct:
        if dct[v][0] > a[0]:
            a = [dct[v][0], v]
    print(f'{place} место:', dct[a[1]][1], a[0])

    for_delete = []
    for value in dct:
        if dct[value][1] == dct[a[1]][1]:
            for_delete.append(value)
    for delete in for_delete:
        dct.pop(delete)