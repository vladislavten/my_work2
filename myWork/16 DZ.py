# Задача 2. Шеренга
# first_line = list(range(160, 176 + 1, 2))
# print('Первая шеренга: ', first_line)
# second_line = list(range(162, 180 + 1, 3))
# print('Вторая шеренга: ', second_line)
#
# first_line.extend(second_line)
#
# for i in range(len(first_line)):
#     for x in range(i, len(first_line)):
#         if first_line[x] < first_line[i]:
#             first_line[x], first_line[i] = first_line[i], first_line[x]
#
# print('\nОтсортированный список:',first_line)


# Задача 3. Детали
# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500],
#         ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
# enter = input('Название детали: ')
# count_detail = 0
# summ = 0
# for i in range(len(shop)):
#         if shop[i][0] == enter:
#                 count_detail += 1
#                 summ += shop[i][1]
# print('\nКол-во деталей:', count_detail)
# print('Общая стоимость:', summ)


# Задача 4. Вечеринка
# guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
# while True:
#     print('\nСейчас на вечеринке', len(guests),  'человек:', guests)
#     choice = input('Гость пришёл или ушёл? ')
#     if choice == 'Пора спать' or choice == 'пора спать':
#         print('Вечеринка закончилась, все легли спать.')
#         break
#     name = input('Имя гостя? ')
#     if choice == 'пришёл' or choice == 'пришел':
#         if len(guests) >= 6:
#             print('Прости,', name, ', но мест нет.')
#         else:
#             print('Привет,', name)
#             guests.append(name)
#     elif choice == 'ушёл' or choice == 'ушел':
#         print('Пока,', name)
#         guests.remove(name)