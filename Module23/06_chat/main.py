# TODO здесь писать код
username = input('Введите имя пользователя: ')

while True:
    print('Выберите действие:'
            '\n1. Посмотреть текущий текст чата'
            '\n2. Отправить сообщение')
    choice = input('ввод: ')
    if choice == '1':
        try:
            with open('chat.txt', 'r', encoding='utf-8') as chat:
                messages = chat.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Файла еще не существует')
    elif choice == '2':
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as chat:
            chat.write(f'{username}: {message}' + '\n')
    else:
        print('Введены не корректные данные\n')
