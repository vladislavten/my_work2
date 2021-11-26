# TODO здесь писать код

n = int(input('Введите кол-во заказов: '))
d = {}
for i in range(1, n + 1):
    order = input(f'{i} заказ: ').split()
    fio, pizza, amount = order[0], order[1], int(order[2])

    if fio not in d:
        d[fio] = {pizza: amount}
    else:
        if pizza not in d[fio]:
            d[fio] |= {pizza: amount}
        else:
            d[fio][pizza] += amount
for fio, order in sorted(d.items()):
    print(f'{fio}:')
    for pizza, amount in sorted(order.items()):
        print('\t', pizza, amount)