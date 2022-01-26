# TODO здесь писать код
from random import choice

card_types = ['A',2,3,4,5,6,7,8,9,10,10,10,10]

player_card = [choice(card_types), choice(card_types)]
diller_card = [choice(card_types), choice(card_types)]
player_flg = False
diller_flg = False

while True:
    player_res = 0
    A_player = []

    for i_card in player_card:
        if isinstance(i_card, int):
            player_res += i_card
        elif isinstance(i_card, str):
            A_player.append(i_card)
    if A_player:
        for i in A_player:
            if player_res < 11:
                player_res += 11
            elif player_res >= 11:
                player_res += 1
    if player_res > 21:
        print('Карты игрока:', player_card)
        print('У вас перебор! Сумма очков:', player_res)
        print('Диллер победил')
        player_flg = True
        break

    print('Карты игрока:', player_card, 'обшая сумма очков:', player_res)

    player_choice = input('\nВыберите действие:\n1 = взять еще карту\n2 = Остановиться\nВвод: ')
    if player_choice == '1':
        player_card.append(choice(card_types))
    elif player_choice == '2':
        while True:
            diller_res = 0
            A_diller = []
            for i_card in diller_card:
                if isinstance(i_card, int):
                    diller_res += i_card
                elif isinstance(i_card, str):
                    A_diller.append(i_card)
            if A_diller:
                for i in A_diller:
                    if diller_res < 11:
                        diller_res += 11
                    elif diller_res >= 11:
                        diller_res += 1
            if diller_res > 21:
                diller_flg = True
                break
            if diller_res < 17:
                diller_card.append(choice(card_types))
            if diller_res >= 17:
                break
        print('Карты игрока:', player_card, 'обшая сумма очков:', player_res)
        print('Карты диллера:', diller_card, 'обшая сумма очков:', diller_res)
        if diller_flg:
            print('Победил игрок!')
        elif player_flg:
            print('Выиграл диллер')
        elif player_res < diller_res:
            print('Выиграл диллер')
        elif player_res > diller_res:
            print('Победил игрок!')
        else:
            print('Ничья')
        break
    else:
        print('Ошибка ввода, выберите 1 или 2')





