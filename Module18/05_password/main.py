# TODO здесь писать код

while True:
    digit_count = 0
    word_count = 0
    word_up_count =0
    password = input('Придумайте пароль: ')
    for i in password:
        if i.isdigit():
            digit_count += 1
        elif i.isalpha():
            word_count += 1
        elif i.isupper():
            word_up_count += 1

    if len(password) >= 8 and digit_count >= 3 and word_count >= 5 and word_up_count >= 1:
        print('Это надёжный пароль!')
        break
    else:
        print('Не надёжный пароль, попробуйте ещё раз')