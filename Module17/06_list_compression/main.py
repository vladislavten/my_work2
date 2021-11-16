# TODO здесь писать код
N = [2, 3, 0, 4, 0, 4, 0, 3, 56, 0, 2, 0, 34, 0, 3]

result = [i for i in N if i > 0]
zeros = [i for i in N if i == 0]
result.extend(zeros)
print(result)