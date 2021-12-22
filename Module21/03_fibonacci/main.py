# TODO здесь писать код
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Номер элемента ряда Фибоначчи: "))
print('Значение этого элемента:', fibonacci(n))