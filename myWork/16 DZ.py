22
# Задача 1. Страшный код

# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
#
# a.extend(b)
# print('Кол-во цифр 5 при первом объединении:', a.count(5))
# for i in range(a.count(5)):
#     a.remove(5)
# a.extend(c)
#
# print('\nКол-во цифр 3 при втором объединении:', a.count(3))
# print('\nИтоговый список:', a)


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
#
#
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
#
#
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


# Задача 5. Песни
# violator_songs = [
# ['World in My Eyes', 4.86],
# ['Sweetest Perfection', 4.43],
# ['Personal Jesus', 4.56],
# ['Halo', 4.9],
# ['Waiting for the Night', 6.07],
# ['Enjoy the Silence', 4.20],
# ['Policy of Truth', 4.76],
# ['Blue Dress', 4.29],
# ['Clean', 5.83]]

# hm_songs = int(input('Сколько песен выбрать? '))
# time = 0
# for i in range(hm_songs):
#     print('Название', i + 1, 'песни:', end = ' ')
#     song_name = input()
#     for i_song in range(len(violator_songs)):
#         if song_name == violator_songs[i_song][0]:
#             time += violator_songs[i_song][1]
#
# print('\nОбщее время звучания песен:', round(time, 2))



# Задача 6. Уникальные элементы
#
# first_list = []
# second_list = []
#
# print('Первый 3 числа')
# for i in range(3):
#     print('Введите', i + 1, 'число:', end = ' ')
#     first = input()
#     first_list.append(first)
#
# print('\nВторые 7 чисел')
# for i in range(7):
#     print('Введите', i + 1, 'число:', end=' ')
#     first = input()
#     second_list.append(first)
#
# first_list.extend(second_list)
# first_list = list(set(first_list))
#
# print('Новый первый список с уникальными элементами:', first_list)



# Задача 7. Ролики
# skates_list = []
# people_list = []
# skates = int(input('Кол-во коньков: '))
# for i in range(skates):
#     print('Размер', i + 1, 'пары:', end = ' ')
#     size = input()
#     skates_list.append(size)
#
# people = int(input('\nКол-во людей: '))
# for i in range(people):
#     print('Размер ноги', i + 1, 'человека:', end = ' ')
#     size = input()
#     people_list.append(size)
#
# count = 0
# for i in people_list:
#     for x in skates_list:
#         if i <= x:
#             count += 1
#             skates_list.remove(x)
#             break
#
# print('Наибольшее кол-во людей, которые могут взять ролики: ', count )


# Задача 8. Считалка

# peoples = int(input('Кол-во человек: '))
# peolpes_list = list(range(1, peoples + 1))
# count_number = int(input('Какое число в считалке? '))
# print('Значит, выбывает каждый', count_number, 'человек')
# a = 0
#
# for i in range(len(peolpes_list) - 1):
#     print('\nТекущий список людей: ', peolpes_list)
#     count = a % len(peolpes_list)
#     a = (count + count_number - 1) % len(peolpes_list)
#     print('начало счета с номера', peolpes_list[count])
#     print('Выбывает человек под номером: ', peolpes_list[a])
#     peolpes_list.remove(peolpes_list[a])
# print()
# print('Остался человек под номером', peolpes_list)


# Задача 9. Друзья
#
# friends = int(input('Кол-во друзей: '))
# friends_list = []
# dolg = int(input('Долговых расписок: '))
#
# for _ in range(friends):
#     friends_list.append(0)
#
# for i in range(dolg):
#     print(i + 1, 'расписка')
#     whom = int(input('Кому: '))
#     From = int(input('От кого: '))
#     hm = int(input('Сколько: '))
#
#     friends_list[whom - 1] -= hm
#     friends_list[From - 1] += hm
#
# print('\nБаланс друзей')
# for num in range(friends ):
#     print(num + 1, ':', friends_list[num])



# Задача 10. Симметричная последовательность

# def is_polindrom(num_list):
#     reverse_list = []
#     for i_num in range(len(num_list) - 1, -1, -1):
#         reverse_list.append(num_list[i_num])
#     if num_list == reverse_list:
#         return True
#     else:
#         return False
#
# nums = [2, 3, 4, 5, 4, 3, 0, 0, 0]
# new_nums = []
# answer = []
#
# for i_nums in range(0, len(nums)):
#     for j_elem in range(i_nums, len(nums)):
#         new_nums.append(nums[j_elem])
#     if is_polindrom(new_nums):
#         for i_answer in range(0, i_nums):
#             answer.append(nums[i_answer])
#         answer.reverse()
#         break
#     new_nums = []
#
# print('Исходный список:', nums)
# print('Нужно чисел для палиндрома:', len(answer))
# print('Список этих чисел:', answer)
