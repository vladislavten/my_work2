# TODO здесь писать код
def check(i):
    if len(i) < 3:
        raise IndexError
    if not i[0].isdigit() or not i[2].isdigit() or (i[1] != '-'
                                                    and i[1] != '+'
                                                    and i[1] != '/'
                                                    and i[1] != '*'
                                                    and i[1] != '//'
                                                    and i[1] != '%'):
        raise ValueError
    if i[2] == '0':
        raise ZeroDivisionError
    if i[1] == '+':
        result = int(i[0]) + int(i[2])
        return result
    if i[1] == '-':
        result = int(i[0]) - int(i[2])
        return result
    if i[1] == '/':
        result = int(i[0]) / int(i[2])
        return result
    if i[1] == '*':
        result = int(i[0]) * int(i[2])
        return result
    if i[1] == '//':
        result = int(i[0]) // int(i[2])
        return result
    if i[1] == '%':
        result = int(i[0]) % int(i[2])
        return result

summ = 0
with open('calc.txt', 'r') as calc:
    for i in calc:
        try:
            print(check(i.split()))
            summ += check(i.split())
        except IndexError:
            print('Недостаточно данных')
        except ValueError:
            print('Ошибка ввода данных')
        except ZeroDivisionError:
            print('Нельзя делить на "0"')

print('Сумма всех ответов:', summ)