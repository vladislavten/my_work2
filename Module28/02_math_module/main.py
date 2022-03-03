import math


class MyMath:
    """
    Математический класс, считающий:
    1. Длину окрыжности
    2. Площадь окружности
    3. Объем куба
    4. Площадь поверхности сферы
    """
    @classmethod
    def circle_len(cls, radius) -> int:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius) -> int:
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, section) -> int:
        return section**3

    @classmethod
    def sphere_area(cls, radius) -> int:
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(section=3)
res_4 = MyMath.sphere_area(radius=10)
print(res_1)
print(res_2)
print(res_3)
print(res_4)


