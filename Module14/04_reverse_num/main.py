# TODO здесь писать код

def reverse(a):
    flg = True
    firstNum = ''
    secondNum = ''
    for i in a:
        if i == '.':
            flg = False
        elif flg :
            firstNum = i + firstNum
        else:
            secondNum = i + secondNum

    e = firstNum + '.' + secondNum
    return(e)


N = input('Введите первое число: ')
K = input('Введите второе число: ')
a = reverse(N)
b = reverse(K)
print('\nПервое число наоборот: ', a)
print('Первое число наоборот: ', b)
print('Сумма ', round(float(a) + float(b), 2))





