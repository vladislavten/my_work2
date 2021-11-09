# TODO здесь писать код
string = [1, 2, 3, 4, 5]
move = int(input('Сдвиг: '))
result = []
print('Изначальный список:', string)

for i in range(len(string)):
    print(i, end = ' ')
    result.append(string[i - move])

print(result)
