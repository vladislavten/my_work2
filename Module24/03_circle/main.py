import math


class Circle:

    def __init__(self, x_coordinate=0, y_coordinate=0, radius=1):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.radius = radius

    def get_area(self):
        print('Площадь равна:', round((self.radius * self.radius * math.pi), 2))

    def get_perimeter(self):
        print('Периметр равен:', round((2 * self.radius * math.pi), 2))

    def scale(self, x_scale):
        self.radius *= x_scale
        print(f'Окружность увеличилась в {x_scale} раз:', self.radius)

    def is_intersect(self, other):
        intersection = (
                    (self.x_coordinate - other.x_coordinate) ** 2 + (self.y_coordinate - other.y_coordinate) ** 2 <= (
                        self.radius + other.radius) ** 2)
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


