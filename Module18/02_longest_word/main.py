# TODO здесь писать код
word = input('Введите слова через пробел: ').split()

result = max((word), key = len)
print('Самое длинное слово: ', result)
print('Количество символов в слове: ', len(result))