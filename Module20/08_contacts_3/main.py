# TODO здесь писать код

phonebook = dict()
while True:
    choice = input('\nВыберите действие: (1) Добавить контакт, (2) Поиск контакта: ')
    if choice == '1':
        IF = input('\nВведите Имя Фамилию через пробел: ').split()
        IF = tuple(IF)
        if IF in phonebook:
            print('Такое имя и фамилия уже есть в телефонной книге')
        else:
            phonenumber = input('Введите номер телефона: ')
            phonebook[IF] = phonenumber
            print('Телефонный справочник:')
            for i, v in phonebook.items():
                print('\t',' '.join(i), v)
    elif choice == '2':
        surname = input('Введите фамилию для поиска: ')
        for name, number in phonebook.items():
            if surname.lower() in name[1].lower():
                print(' '.join(name), number)
    else:
        print('Ошибка ввода!')