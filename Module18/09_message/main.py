# TODO здесь писать код
message = input('Введите сообщение: ')
word = ''
result = ''
for i in message:
    if i.isalpha():
        word += i
    elif not i.isalpha():
        word = word[::-1]
        result += word
        result += i
        word = ''
if len(word) >= 1:
    print('Результат:', word[::-1])
else:
    print('Результат:', result)