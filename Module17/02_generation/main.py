# TODO здесь писать код
import random
N = int(input('Введите число: '))

lst_N = [random.randint(1, 100) for _ in range(N)]
lst_N = [1 if i % 2 == 0 else i % 5 for i in range(0, len(lst_N))]

print('Результат:', lst_N)