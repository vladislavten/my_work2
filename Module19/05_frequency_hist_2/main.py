# TODO здесь писать код

text = input('Введите текст: ')
dct = dict()
dct_invert = dict()
for i in text:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

for i in sorted(dct):
    print(i, ':', dct[i])


for i in dct:
    if dct[i] in dct_invert:
        dct_invert[dct[i]].append(i)
    else:
        dct_invert[dct[i]] = [i]

print('\nИнвертированный словарь частот:')

for i in dct_invert:
    print(i, ':', dct_invert[i])