import timeit

res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(res)

print(timeit.timeit('[str(n) for n in range(100)]', number=10000))
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))
