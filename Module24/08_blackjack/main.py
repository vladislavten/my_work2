from random import choice


class Cards:
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def __init__(self, cards):
        cards.extend([choice(self.cards), choice(self.cards)])

    def one_card(self, cards):
        cards.extend([choice(self.cards)])

    @staticmethod
    def count(cards):
        result = 0
        ace = []
        for i_card in cards:
            if isinstance(i_card, int):
                result += i_card
            elif isinstance(i_card, str):
                ace.append(i_card)
        if ace:
            for _ in ace:
                if result < 11:
                    result += 11
                elif result >= 11:
                    result += 1
        return result


player_card = []
casino_card = []

player = Cards(player_card)
casino = Cards(casino_card)

player_flg = False
casino_flg = False

while True:
    if player.count(player_card) > 21:
        print('Карты игрока:', player_card)
        print('У вас перебор! Сумма очков:', player.count(player_card))
        print('Диллер победил')
        player_flg = True
        break

    print('Карты игрока:', player_card, 'обшая сумма очков:', player.count(player_card))

    player_choice = input('\nВыберите действие:\n1 = взять еще карту\n2 = Остановиться\nВвод: ')
    if player_choice == '1':
        player.one_card(player_card)
    elif player_choice == '2':

        while True:
            if casino.count(casino_card) > 21:
                casino_flg = True
                break
            if casino.count(casino_card) >= 17:
                break
            if casino.count(casino_card) < 17:
                casino.one_card(casino_card)

        print('Карты игрока:', player_card, 'обшая сумма очков:', player.count(player_card))
        print('Карты диллера:', casino_card, 'обшая сумма очков:', casino.count(casino_card))
        if casino_flg:
            print('Выиграл игрок!')
        elif player_flg:
            print('Выиграл диллер!')
        elif player.count(player_card) < casino.count(casino_card):
            print('Выиграл диллер!')
        elif player.count(player_card) > casino.count(casino_card):
            print('Выиграл игрок!')
        else:
            print('Ничья')
        break
    else:
        print('Ошибка ввода, выберите 1 или 2')
