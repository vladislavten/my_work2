# TODO здесь писать код
file = open('people.txt', 'r').read().split()

for i, value in enumerate(file):
    try:
        if len(value) < 3:
            raise ValueError
        else:
            print(len(value))
    except ValueError:
        with open('errors.log', 'a', encoding='utf-8') as file:
            result = f'Ошибка в {i + 1} строке. Меньше трёх символов'
            file.write(str(result) + '\n')
