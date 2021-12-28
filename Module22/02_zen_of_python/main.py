# TODO здесь писать код

zen = open('zen.txt', 'r')
lst_zen = []

for i in zen:
    lst_zen.append(i[:-2])

for x in lst_zen[::-1]:
    print(x)
