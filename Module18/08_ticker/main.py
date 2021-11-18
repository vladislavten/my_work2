# TODO здесь писать код
first_str = list(input('Первая строка: '))
second_str = list(input('Вторая строчка строка: '))
result = []

count = -1
flg = True
for i in first_str:
    if flg == False:
        break
    for x in second_str:
        count += 1
        if i == x:
            flg = False
            break

for y in range(len(first_str)):
    result.append(first_str[y - count])

if result == second_str:
    print('\nПервая строка получается из второй со сдвигом', count)
else:
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
