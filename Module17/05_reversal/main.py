# TODO здесь писать код
string = input('Введите слово с двумя "h": ')
first = string.index('h')
last = string.rindex('h')
print('Результат:', (string[first + 1:last])[::-1])