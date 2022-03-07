



print(' '.join(['-' if i % j == 0 else str(i) for i in range(2, 100+1) for j in range(2, i)]))


lst = []
for i in range(2, 100+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(str(i))

print(' '.join(lst))
