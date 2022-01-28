# TODO здесь писать код
import math


class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def get_area(self):
        print('Площадь равна:', round((self.r * self.r * math.pi),2))

    def get_perimeter(self):
        print('Периметр равен:', 2 * self.r * math.pi)

    def scale(self, k):
        self.r *= k
        print(f'Окружность увеличилась в {k} раз:', self.r)

    def is_intersect(self, other):
        intersection = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2)
        if intersection:
            print('Окружности пересекаются')
        else:
            print('Окружности не пересекаются')


circle = Circle(-2, 8, 2)
circle2 = Circle(9, 20, 1)
circle.get_area()
circle.scale(5)
circle.get_perimeter()
circle.is_intersect(circle2)

# TODO однобуквенных переменнных быть недолжно
