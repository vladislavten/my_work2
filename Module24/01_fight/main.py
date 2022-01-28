import random


class Fight:

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def test_health(self):
        if self.health <= 0:
            return True

    def self_kick(self):
        self.health -= 20


warrior_1 = Fight('Воин_1')
warrior_2 = Fight('Воин_2')

while warrior_1.health > 0 and warrior_2.health > 0:
    rand = random.randint(1, 2)
    if rand == 1:
        warrior_2.self_kick()
        print(f'{warrior_1.name} {warrior_1.health} атаковал, {warrior_2.name} {warrior_2.health}')
    elif rand == 2:
        warrior_1.self_kick()
        print(f'{warrior_2.name} {warrior_2.health} атаковал, {warrior_1.name} {warrior_1.health}')
    if warrior_1.test_health():
        print('Победил', warrior_2.name)
    elif warrior_2.test_health():
        print('Победил', warrior_1.name)

123