

class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('картошка {} сейчас {} '.format(self.index, Potato.states[self.state]))

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class PotatosGarden:
    def __init__(self,count):
        self.potatos = [Potato(index) for index in range(1,count + 1)]
        self.count = count

    def grow_all(self):
        print(f'Картошка прорастает')

        for i_potato in self.potatos:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatos]):
            print('картошка еще не созрела\n')
        else:
            print('картошка созрела\n')
            print('картошку собрал ', name_gardener.name, 'в количестве ', self.count )


class Gardener:
    def __init__(self, name):
        self.name = name
        print(f'За картошкой ухаживает {self.name}')

    def care(self):
        my_garden.are_all_ripe()
        for i_count in range(3):
            my_garden.grow_all()
            my_garden.are_all_ripe()


name_gardener = Gardener('Дядя Вася')
my_garden = PotatosGarden(5)
name_gardener.care()