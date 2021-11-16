# TODO здесь писать код
sticks = int(input('Кол-во палок: '))
throws = int(input('Кол-во бросков: '))

lst = ['|' for i in range(sticks)]

for i in range(1, throws + 1):
    print('Бросок', i, '. ', end = '')
    print('Сбиты палки с номера', end = '')
    a = int(input(' '))
    print('по номер', end = '')
    b = int(input(' '))
    for z in range (a - 1, b):
        lst[z] = '.'

for i in lst:
    print(i, end = '')