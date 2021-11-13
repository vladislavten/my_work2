# TODO здесь писать код
skates_list = []
people_list = []
skates = int(input('Кол-во коньков: '))
for i in range(skates):
    print('Размер', i + 1, 'пары:', end = ' ')
    size = input()
    skates_list.append(size)

people = int(input('\nКол-во людей: '))
for i in range(people):
    print('Размер ноги', i + 1, 'человека:', end = ' ')
    size = input()
    people_list.append(size)

count = 0
for i in people_list:
    for x in skates_list:
        if i <= x:
            count += 1
            skates_list.remove(x)
            break

print('Наибольшее кол-во людей, которые могут взять ролики: ', count )
