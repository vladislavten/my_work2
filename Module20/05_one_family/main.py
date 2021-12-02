# TODO здесь писать код

family = {
    ("Сидоров", "Никита"): 35,
    ("Сидорова", "Алина"): 34,
    ("Сидоров", "Павел"): 10,
    ("Веселов", "Евгений"): 32,
    ("Веселова", "Виктория"): 29,
    ("Веселов", "Роман"): 5,
    ("Иванов", "Иван"): 45,
    ("Иванова", "Светлана"): 40,

}
print('')
surname = input('Введите фамилию: ')
if surname[-1:] == 'а':
    surname2 = surname[:-1]
else:
    surname2 = surname + 'а'

for i, v in family.items():
    if surname in i:
        print(' '.join(i), v)
    elif surname2 in i:
        print(' '.join(i), v)