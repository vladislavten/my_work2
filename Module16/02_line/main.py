# TODO здесь писать код
first_line = list(range(160, 176 + 1, 2))
print('Первая шеренга: ', first_line)
second_line = list(range(162, 180 + 1, 3))
print('Вторая шеренга: ', second_line)

first_line.extend(second_line)

for i in range(len(first_line)):
    for x in range(i, len(first_line)):
        if first_line[x] < first_line[i]:
            first_line[x], first_line[i] = first_line[i], first_line[x]

print('\nОтсортированный список:',first_line)