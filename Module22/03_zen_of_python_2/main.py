# TODO здесь писать код

zen = open('zen.txt', 'r')
a = 0
str_count = 0
words_count = 0
min_letter = {}
data = zen.read()

letter_count = [i_letter.lower() for i_letter in data if i_letter.isalpha()] #Считаю буквы

for y in letter_count:
    if y in min_letter:
        min_letter[y] += 1
    else:
        min_letter[y] = 1

zen = open('zen.txt', 'r') #Не понял почему необходимо еще раз открывать уже открытый файл???

for i in zen: #Считаем строки
    str_count +=1

for i in data.split(): #Считаем слова
    words_count += 1

# one_min_letter = ''
# for index, value in min_letter.items():
#     if value == min(min_letter.values()):
#         one_min_letter = index

one_min_letter = [index for index, value in min_letter.items() if value == min(min_letter.values())]

print('Количество букв в файле:', len(letter_count))
print('Количество слов в файле:', words_count)
print('Количество строк в файле:', str_count)
print('Наиболее редкая буква:', one_min_letter)


