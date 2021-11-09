# TODO здесь писать код

word = input('Введите слово: ')
word = list(word)
result = 0

for i in range(len(word) ):
    count = 0
    for x in word:
        if x == word[i]:
            count +=1
    if count == 1:
        result += 1

print('Кол-во уникальных букв:',result)
