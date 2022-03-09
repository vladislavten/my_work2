# 30.4 Lambda-функции
# Задача 1. Минимум и максимум
# from typing import Union, Dict
#
# grades: Dict[str, Union[str, int]] = [{'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41}, {'name': 'Joyce', 'score': 24}, {'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
#
# {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},
#
# {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},
#
# {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},
#
# {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},
#
# {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},
#
# {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},
#
# {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},
#
# ]
#
# print(min(grades, key=lambda elem: elem['score']))
# print(max(grades, key=lambda elem: elem['score']))




# 30.5 Функции map и filter
# Задача 1. Однострочный код

# print(sorted(input('Введите число через пробел: ').split(' ')))





# Задача 2. Однострочный код 2

# print([i for i in input('Введите текст: ') if i.isalpha() and i.islower()])





# Задача 3. Функция reduce
#
# Помимо map и filter, есть ещё одна функция — reduce. Она применяет указанную функцию к
# элементам последовательности, сводя её к единственному значению. Однако используют reduce
# довольно редко. Начиная с третьей версии Python, эту функцию даже вынесли из встроенных
# функций в модуль functools.


# from functools import reduce
# from typing import List
#
#
# def my_add(a: int, b: int) -> int:
#     result = a + b
#     print(f"{a} + {b} = {result}")
#     return result
#
#
# numbers: List[int] = [0, 1, 2, 3, 4]
#
# print(reduce(my_add, numbers))


############ ТЕСТ работы lambda и map и filter ######################

# a = [1,2,3,4,5]
# b =[6,7,8,9, 5]
#
# print(list(map(lambda x, y: x * y, a, b)))
#
# print(list(filter(lambda x: x == 5, b)))

import TIMER

if __name__ == '__main__':
    print('1')

