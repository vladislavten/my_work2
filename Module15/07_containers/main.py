# TODO здесь писать код

number = int(input('Кол-во контейнеров: '))
containers = []
count = 1

for _ in range(number):
    weight = int(input('Введите вес контейнера: '))
    if weight > 200:
        print('Ошибка. Вес не полжен превышать 200')
    else:
        containers.append(weight)

new_weight = int(input('\nВведите вес нового контейнера: '))

for i in containers:
    if i >= new_weight:
        count += 1

print('\nНомер, куда встанет новый контейнер:', count)


