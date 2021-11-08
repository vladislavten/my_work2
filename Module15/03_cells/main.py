# TODO здесь писать код

cell = int(input('Количество клеток: '))
result = []

for i in range(cell):
    print('Эффективность', i + 1, 'клетки:', end = ' ')
    rang = int(input())
    if rang < i:
        result.append(rang)
print(result)