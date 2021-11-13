guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код
while True:
    print('\nСейчас на вечеринке', len(guests),  'человек:', guests)
    choice = input('Гость пришёл или ушёл? ')
    if choice == 'Пора спать' or choice == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    name = input('Имя гостя? ')
    if choice == 'пришёл' or choice == 'пришел':
        if len(guests) >= 6:
            print('Прости,', name, ', но мест нет.')
        else:
            print('Привет,', name)
            guests.append(name)
    elif choice == 'ушёл' or choice == 'ушел':
        print('Пока,', name)
        guests.remove(name)