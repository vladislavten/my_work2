# TODO здесь писать код

number = {str(i) for i in range(1, int(input('Введите максимальное число: ')) + 1)}
while True:
    choice = input('Нужное число есть среди вот этих чисел: ')
    if choice == 'Помогите':
        print('Артём мог загадать следующие числа:', sorted(number))
        break
    choice = choice.split(' ')
    choice = set(choice)
    answer = input('Ответ Артёма: ')
    if answer == 'Да' or answer == 'да':
        number = number & choice
    elif answer == 'нет' or answer == 'Нет':
        number = number - choice


