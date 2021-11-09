# TODO здесь писать код

word = input('Введите слово: ')
result = ''

for i in word:
    result = i + result

if word == result:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')




