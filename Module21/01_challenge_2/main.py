# TODO здесь писать код
def count(start):
    if start == 1:
        return start
    print(count(start - 1))
    return start

num = int(input('Введите число: '))
count(num + 1)