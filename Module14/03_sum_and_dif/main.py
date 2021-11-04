
def Nsumm(a):
    a =str(a)
    DigitSumm = 0
    for i in a:
        i = int(i)
        DigitSumm += i
    print('Сумму всех цифр: ', DigitSumm)
    return(DigitSumm)

def summDigits(a):
    a = str(a)
    count = 0
    for i in a:
        count += 1
    print('Количество цифр в числе: ', count)
    return(count)

N = int(input('Введите число: '))
a = Nsumm(N)
b = summDigits(N)
print('Разность суммы и кол-ва цифр:50', a - b)
