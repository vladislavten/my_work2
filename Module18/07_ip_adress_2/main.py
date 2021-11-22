# TODO здесь писать код
ip = input('Введите IP: ').split('.')
flg = True

for i in ip:
    if not i.isdigit() and flg:
        print(i, 'не целое число')
        flg = False
        break
    elif int(i) > 255:
        print(i, 'превышает 255')
        flg = False
        break
    elif len(ip) != 4:
        print('Адрес - это четыре числа, разделённые точками')
        flg = False
        break

if flg == True:
    print('Корректный IP адрес')
