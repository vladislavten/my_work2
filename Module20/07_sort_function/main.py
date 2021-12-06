# TODO здесь писать код

def sort(cort):
    for i in cort:
        if not isinstance(i, int):
            return cort
    return tuple(sorted(cort))

# ПЕРЕМЕННЫЕ НА ВЫБОР
# cort = (1, 8, 17, 9, 20, 13, 2, 6, 20, 11, 7, 19, 13, 3, 7)
cort = (1, 8, 17, 9, 20, 13, 2.3, 6, 20, 11, 7, 19, 13, 3, 7)

print(sort(cort))
