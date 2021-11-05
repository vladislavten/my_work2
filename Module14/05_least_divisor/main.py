# TODO здесь писать код

N = int(input('Введите число: '))
for i in range(2, N + 1):
    a = 0
    if N % i == 0:
        a = i
        break
print('Наименьший делитель, отличный от единицы: ', a)