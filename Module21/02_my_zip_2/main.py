# TODO здесь писать код
def my_zip(*arg):
    arg = list(map(list, arg))
    try:
        yield tuple(map(lambda x : x.pop(0), arg))
        yield from my_zip(*arg)
    except:
        pass

first_cort = (1, 2, 3)
second_cort = (11, 22, 33, 44)

print(*my_zip(first_cort, second_cort))
