# TODO здесь писать код

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_lst = []

for i in range(int(len(lst) / 2)):
    new_lst.append(tuple(lst[:2]))
    lst.remove(lst[0])
    lst.remove(lst[0])

print(new_lst)


# ВТОРОЙ ВАРИАНТ

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_lst = []
count = 0
for i in range(int(len(lst) / 2)):
    new_lst.append(tuple(lst[count:2 + count]))
    count += 2

print(new_lst)
