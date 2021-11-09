# TODO здесь писать код

number = int(input('Введите кол-во видеокарт: '))
models = []
result = []
_ = True
for i in range(number):
    print(i + 1, 'Видеокарта:', end = ' ')
    model = int(input())
    models.append(model)

print('Старый список видеокарт: ', models)

for x in models:
    if x != max(models):
        result.append(x)

print('Новый список видеокарт:', result)