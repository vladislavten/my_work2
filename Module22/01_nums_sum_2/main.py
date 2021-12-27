# TODO здесь писать код

num = open('numbers.txt', 'r')
summ = 0
flg = True

for i_num in num:
    if i_num == '\n':
        flg = False
    else:
        summ += int(i_num)
num.close()

summ = str(summ)
answer = open('answer.txt', 'w')
answer.write(summ)

answer = open('answer.txt', 'r')
data = answer.read()
answer.close()

print('Содержимое файла answer.txt')
print(data)

