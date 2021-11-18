# TODO здесь писать код
# import random
# first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
# second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
#
# result = [first_team[i] if first_team[i] > second_team[i] else second_team[i] for i in range(20)]
#
# print('Первая команда:', first_team)
# print('\nВторая команда:', second_team)
# print('\nПобедители тура:', result)

import random

s1 = [round(random.uniform(5,10),2) for x in range(20)]
s2 = [round(random.uniform(5,10),2) for x in range(20)]
s3 = [s1 if s1 >= s2 else s2 for x in range(20)]

result = []

print(s1)
print(s2)
print(s3)