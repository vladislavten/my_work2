# TODO здесь писать код
dct = dict()

for i in range(1, (int(input('Введите количество пар слов: '))) + 1):
    pair = input('{} пара: '.format(i)).split(' - ')
    dct[pair[0]] = pair[1]
    dct[pair[1]] = pair[0]

while True:
    word = input('Введите слово: ')
    if dct.get(word):
        print('Синоним: ', dct[word])
    else:
        print('Такого слова в словаре нет.')