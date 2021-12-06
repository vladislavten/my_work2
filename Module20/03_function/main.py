# TODO здесь писать код

def func(cort, elem):
    new_cort = []
    index =[]

    for i, y in enumerate(cort):
        if y == elem:
            index.append(i)
    if len(index) >= 2:
        new_cort.extend(cort[index[0]:index[1]+1])
    elif len(index) == 1:
        new_cort.extend(cort[index[0]:])

    return tuple(new_cort)

cort= ('с', 'а', 'й', 'г', 'а', '4', 'т', 'ж', 'н', 'Й')

print('Дан кортеж: ', cort)
elem = input('Введите элемент: ')

print('\n', func(cort, elem))