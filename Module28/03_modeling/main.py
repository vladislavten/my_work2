from abc import ABC, abstractmethod
import math


class Figure(ABC):
    """
    Абстрактный класс для фигуры
    """

    def __init__(self, x_len: int, y_len: int):
        self._x_len = x_len
        self._y_len = y_len

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):
    """
    Класс Квадрат - родительский класс Figure
    Класс вычисляет Площадь квадрата, Периметр квадрата, Площадь Куба
    """
    def __init__(self, x_len: int):
        super().__init__(x_len, x_len)

    @property
    def x_len(self):
        return self._x_len

    @x_len.setter
    def x_len(self, x_len: int):
        self._x_len = x_len

    def area(self) -> int:
        return self._x_len * self._x_len

    def perimeter(self) -> int:
        return (self._x_len + self._x_len) * 2

    def cube_safe(self) -> list:
        return [self._x_len for _ in range(6)]

    def cube_area(self) -> int:
        return self._x_len * 6


class Triangle(Figure):
    """
    Класс треугольника. Родительский класс Figure
    Класс вычисляет Площадь треугольника, Периметр треугольника, Площадь Пирамиды
    x_len = Основание
    y_len = Высота
    """
    @property
    def x_len(self):
        return self._x_len

    @x_len.setter
    def x_len(self, x_len: int):
        self._x_len = x_len

    @property
    def y_len(self):
        return self._y_len

    @y_len.setter
    def y_len(self, y_len: int):
        self._y_len = y_len

    def area(self) -> float:
        return 1 / 2 * self._x_len * self._y_len

    def perimeter(self) -> float:
        return math.sqrt(self._x_len**2 + (self._y_len/2)**2) * 2 + self._y_len

    def pyramid_safe(self) -> list:
        area = 1 / 2 * self._x_len * self._y_len
        return [area for _ in range(4)]

    def pyramid_area(self) -> float:
        return (1 / 2 * self._x_len * self._y_len) * 4


square = Square(5)
print('Сторона квадрата равна:', square.x_len)
print('Площадь квадрата: {},   Периметр квадрата: {}'.format(square.area(), square.perimeter()))
print('Куб хранится в виде: {}, Площадь куба: {}'.format(square.cube_safe(), square.cube_area()))
square.x_len = 8
print('\nСторона квадрата равна:', square.x_len)
print('Площадь квадрата: {},   Периметр квадрата: {}'.format(square.area(), square.perimeter()))
print('Куб хранится в виде: {}, Площадь куба: {}'.format(square.cube_safe(), square.cube_area()))

triangle = Triangle(10, 5)
print('\nВысота треугольника: {},  Основание треугольника: {}'.format(triangle.x_len, triangle.y_len))
print('Площадь треугольника: {},  Периметр треугольника: {}'.format(triangle.area(), round(triangle.perimeter() , 2)))
print('Пирамида хранится в виде: {}, Площадь куба: {}'.format(triangle.pyramid_safe(), triangle.pyramid_area()))

triangle.x_len = 15
triangle.y_len = 12
print('\nВысота треугольника: {},  Основание треугольника: {}'.format(triangle.x_len, triangle.y_len))
print('Площадь треугольника: {},  Периметр треугольника: {}'.format(triangle.area(), round(triangle.perimeter(), 2)))
print('Пирамида хранится в виде: {}, Площадь куба: {}'.format(triangle.pyramid_safe(), triangle.pyramid_area()))

























