class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            print('None')


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()


class Fire:
    def __str__(self):
        return 'огонь'


class Earth:
    def __str__(self):
        return 'земля'


class Storm:
    def __str__(self):
        return 'шторм'


class Vapor:
    def __str__(self):
        return 'пар'


class Dirt:
    def __str__(self):
        return 'грязь'


water = Water()
air = Air()
fire = Fire()
earth = Earth
print(air + fire)
