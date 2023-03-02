# MyProfile app

SEPARATOR = '-' * 47

# user profile
name = ''
age = 0
phone = ''
email = ''
info = ''
index = ''
address = ''
# social links
ogrnip = 0
iin_number = 0
checking_account = 0
bank_name = ''
bik = 0
correspondent_account = ''


def general_info_user(name_parameter,
                      age_parameter,
                      phone_parameter,
                      email_parameter,
                      index_parameter,
                      address_parameter,
                      info_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс: ', index_parameter)
    print('Адрес:  ', address_parameter)
    if info:
        print('')
        print('Дополнительная информация:')
        print(info_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = input('Введите номер пункта меню: ')
    if option == '0':
        break

    if option == '1':
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option_2 = input('Введите номер пункта меню: ')
            if option_2 == '0':
                break
            if option_2 == '1':
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    try:
                        age = int(input('Введите возраст: '))
                        if age > 0:
                            break
                        print('Возраст должен быть положительным')
                    except:
                        print('Введите корректные данные')

                User_Phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for i in User_Phone:
                    if i == '+' or ('0' <= i <= '9'):
                        phone += i

                email = input('Введите адрес электронной почты: ')
                index_check = input('Введите почтовый индекс: ')
                index += ''.join([i for i in index_check if i.isdigit()])
                address = input('Введите почтовый адрес (без индекса): ')
                info = input('Введите дополнительную информацию:\n')

            elif option_2 == '2':
                # input social links
                stop = True
                while stop:
                    try:
                        ogrnip = int(input('Введите номер ОГРНИП: '))
                        if len(str(ogrnip)) == 15 and str(ogrnip).isdigit():
                            while stop:
                                try:
                                    iin_number = int(input('Введите номер ИИН: '))
                                    while stop:
                                        try:
                                            checking_account = int(input('Введите расчётный счёт: '))
                                            if len(str(checking_account)) == 20 and str(checking_account).isdigit():
                                                bank_name = input('Введите название банка: ')
                                                while stop:
                                                    try:
                                                        bik = int(input('Введите БИК: '))
                                                        while stop:
                                                            try:
                                                                correspondent_account = int(input('Введите корреспондентский счёт: '))
                                                                stop = False
                                                            except:
                                                                print('Введены не корректные данные корреспондентского счёта')

                                                    except:
                                                        print('Введены не корректные данные БИК')
                                        except:
                                            print('Введены не корректные данные расчетного счёта')
                                except:
                                    print('Введите корректные данные ИИН')
                        else:
                            print('Введены не корректные данные ОГРНИП')
                    except:
                        print('Введите корректные данные')
            else:
                print('«Введён некорректный пункт меню')
    elif option == '2':
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option_2 = input('Введите номер пункта меню: ')
            if option_2 == '0':
                break
            if option_2 == '1':
                general_info_user(name,
                                  age,
                                  phone,
                                  email,
                                  index,
                                  address,
                                  info)

            elif option_2 == '2':
                general_info_user(name,
                                  age,
                                  phone,
                                  email,
                                  index,
                                  address,
                                  info)

                # print social links
                print('')
                print('Информация о предпринимателе:')
                print('ОГРНИП: ', ogrnip)
                print('ИИН:    ', iin_number)
                print('Банковские реквизиты')
                print('Р/с:    ', checking_account)
                print('Банк:   ', bank_name)
                print('БИК:    ', bik)
                print('К/с:    ', correspondent_account)
            else:
                print('«Введён некорректный пункт меню')
    else:
        print('«Введён некорректный пункт меню')
