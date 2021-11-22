# TODO здесь писать код
s = input('Введите строку: ')
count = 0
result = ''

for i in range(len(s)):
    count += 1
    if i == len(s) - 1:
        result = result + s[i] + str(count)
        break
    if s[i] != s[i+1]:
        result = result + s[i] + str(count)
        count = 0

print('Сжатый вариант: ', result)