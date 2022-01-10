# TODO здесь писать код
username = input('Введите имя пользователя: ')
with open('chat.txt', 'a', encoding='utf-8') as chat:
    while True:
        print('Выберите действие:'
              '\n1. Посмотреть текущий текст чата'
              '\n2. Отправить сообщение')
        choice = input('ввод: ')
        if choice == '1':
            with open('chat.txt', 'r', encoding='utf-8') as chat:
                for i_line in chat:
                    print('\t', i_line, end='')

        elif choice == '2':
            with open('chat.txt', 'a', encoding='utf-8') as chat:
                message = input('Введите сообщение: ')
                chat.write(f'{username}: {message}' + '\n')
        else:
            print('Введены не корректные данные\n')
