# TODO здесь писать код
def summ(*args):
    return sum(summ(*a) if isinstance(a, list) else a for a in args)

print(summ(1, 2, 8, 4, 9))
print(summ([[1, 2, [3]], [4], 5]))