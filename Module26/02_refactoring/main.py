def find_number() -> int:
    for x in list_1:
        for y in list_2:
            result = x * y
            print('{} * {} = {}'.format(x, y, result))
            if result == to_find:
                yield result


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

find = find_number()
for i_num in find:
    print('Число {} найдено'.format(to_find))
    break
