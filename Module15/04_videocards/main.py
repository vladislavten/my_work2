# TODO здесь писать код

number = int(input('Введите кол-во видеокарт: '))
count = 1
models = []
result = []
_ = True
for i in range(number):
    print(count, 'Видеокарта:', end = ' ')
    model = int(input())
    models.append(model)
    count += 1

print('Старый список видеокарт: ', models)

for x in models:
    if x == max(models):
        _ = False
    else:
        result.append(x)

print('Новый список видеокарт:', result)