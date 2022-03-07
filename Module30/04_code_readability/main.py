print(list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))), range(2, 100 + 1))))

result = []
for i in range(2, 100+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        result.append(str(i))

print(' '.join(result))
