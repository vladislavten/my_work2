# TODO здесь писать код

peoples = int(input('Кол-во человек: '))
peolpes_list = list(range(1, peoples + 1))
count_number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', count_number, 'человек')
a = 0

for i in range(len(peolpes_list) - 1):
    print('\nТекущий список людей: ', peolpes_list)
    count = a % len(peolpes_list)
    a = (count + count_number - 1) % len(peolpes_list)
    print('начало счета с номера', peolpes_list[count])
    print('Выбывает человек под номером: ', peolpes_list[a])
    peolpes_list.remove(peolpes_list[a])
print()
print('Остался человек под номером', peolpes_list)