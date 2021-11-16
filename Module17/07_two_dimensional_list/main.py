# TODO здесь писать код

import random
def generate():
    lst = [random.randint(1, 15) for _ in range(3)]
    return lst

result = [generate() for _ in range(4)]

print('Результат:', result)