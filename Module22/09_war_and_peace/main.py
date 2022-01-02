# TODO здесь писать код
import zipfile
archive = zipfile.ZipFile('voyna-i-mir.zip', 'r')
archive.extractall() # Извлечь файл из архива

word_count = {}
sorted_dict = {}
voynaimir = open('voyna-i-mir.txt', 'r', encoding='utf-8').read()

letter_count = [i_letter for i_letter in voynaimir if i_letter.isalpha()] #Считаю буквы

for y in letter_count:
    if y in word_count:
        word_count[y] += 1
    else:
        word_count[y] = 1

sorted_values = sorted(word_count.values(), reverse=True)

for i in sorted_values:
    for k in word_count.keys():
        if word_count[k] == i:
            sorted_dict[k] = word_count[k]
            break

for letter, count in sorted_dict.items():
    print(letter, count)
