# TODO здесь писать код
friends = int(input('Кол-во друзей: '))
friends_list = []
dolg = int(input('Долговых расписок: '))

for _ in range(friends):
    friends_list.append(0)

for i in range(dolg):
    print(i + 1, 'расписка')
    whom = int(input('Кому: '))
    From = int(input('От кого: '))
    hm = int(input('Сколько: '))

    friends_list[whom - 1] -= hm
    friends_list[From - 1] += hm

print('\nБаланс друзей')
for num in range(friends ):
    print(num + 1, ':', friends_list[num])
