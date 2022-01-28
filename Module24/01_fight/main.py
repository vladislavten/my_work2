
import random


# TODO должны быть реализованы методы
# TODO __init__ чтобы можно было создать экземпляр класса
# TODO этот метод должен принимать парметры имя, и параметр колличестов здоровья по умолчанию 100
# TODO + два метода:
# TODO проверки себя на жизнь
# TODO метод который ударяет себя, уменьшает жизнь на заданную величину
class Fight:

     def __init__(self, name, health):
        self.name = name
        self.health = health

     def fight_warriors(self):
        while warrior_1.health > 0 and warrior_2.health > 0:
            rand = random.randint(1, 2)
            if rand == 1:
                warrior_2.health -= 20
                print('Воин_1 {} атаковал, Воин_2 {}'.format(warrior_1.health, warrior_2.health))
            elif rand == 2:
                warrior_1.health -= 20
                print('Воин_2 {} атаковал, Воин_1 {}'.format(warrior_2.health, warrior_1.health))
            if  warrior_1.health <= 0:
                print('Победил', warrior_2.name)
            elif warrior_2.health <= 0:
                print('Победил', warrior_1.name)

# TODO логика боя должна быть написана тут
warrior_1 = Fight('Воин_1', 100)
warrior_2 = Fight('Воин_2', 100)
warrior_1.fight_warriors()

# TODO есть недочеты по PEP подчеркивания и выделения кода быть недолжно
# TODO используйте в некоторых случаях code - reformat code
