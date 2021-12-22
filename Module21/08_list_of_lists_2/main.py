nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# TODO здесь писать код

def summ(nice_list, result = []):
    for i in nice_list:
        if isinstance(i, list):
            summ(i)
        else:
            result.append(i)
    return result

print(summ(nice_list))
