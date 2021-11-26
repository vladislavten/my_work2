goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код
for i in goods:
    summ = 0
    quantity = 0
    if goods[i] in store:
        for y in range(len(store[goods[i]])):
            summ += store[goods[i]][y]['quantity'] * store[goods[i]][y]['price']
            quantity += store[goods[i]][y]['quantity']
        print('{} - {} шт, стоимость {} руб'.format(i, quantity, summ))