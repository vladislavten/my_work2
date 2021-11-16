# TODO здесь писать код
vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']

text = input('Введите текст: ')
result = [letter for letter in text for x in vowels if letter == x]

print('Список гласных букв: ', result)
print('Длина списка:', len(result))