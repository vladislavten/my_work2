# TODO здесь писать код

import random

r, f = 0, open('nums.txt', 'w')

with f as file:
        try:
            while r <= 777:
                n = int(input('Введите число: '))
                r += n
                if random.choices((0, 1), (1-1/13, 1/13))[0]:
                    raise AttributeError
                print(n, file=file)
        except:
            print('Вас постигла неудача!')

        if r >= 777:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')
