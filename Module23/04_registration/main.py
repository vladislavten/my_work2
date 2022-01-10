# TODO здесь писать код
def func(line):
    if line == []:
        raise Exception
    if len(line) < 3:
        raise IndexError
    for i in line[0]:
        if not i.isalpha():
            raise NameError
    if not '@' in line[1] and not '.' in line[1]:
        raise SyntaxError
    if int(line[2]) < 10 or int(line[2]) > 100:
        raise ValueError
    else:
        res = ''.join(i_line[:-1]) + '\n'
        with open('registrations_good.log', 'a', encoding='utf-8') as file:
            file.write(str(res))


registr = open('registrations.txt', 'r', encoding = 'utf-8')
for i_line in registr:
    try:
        func(i_line.split())
    except IndexError:
        res = ''.join(i_line[:-1]) + '\t\tНЕ присутствуют все три поля' + '\n'
        with open('registrations_bad.log', 'a', encoding='utf-8') as file:
            file.write(str(res))
    except NameError:
        res = ''.join(i_line[:-1]) + '\t\tполе имени содержит НЕ только буквы' + '\n'
        with open('registrations_bad.log', 'a', encoding='utf-8') as file:
            file.write(str(res))
    except SyntaxError:
        res = ''.join(i_line[:-1]) + '\t\tполе емейл НЕ содержит @ и .(точку)' + '\n'
        with open('registrations_bad.log', 'a', encoding='utf-8') as file:
            file.write(str(res))
    except ValueError:
        res = ''.join(i_line[:-1]) + '\t\tполе возраст НЕ является числом от 10 до 99:' + '\n'
        with open('registrations_bad.log', 'a', encoding='utf-8') as file:
            file.write(str(res))
    except Exception:
        res = ''.join(i_line[:-1]) + '.......' + '\n'
        with open('registrations_bad.log', 'a', encoding='utf-8') as file:
            file.write(str(res))

