# TODO здесь писать код
import math

class Circle:


    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def get_area(self):
        print(self.r * self.r * math.pi)

    def get_perimeter(self):
        print( 2 * self.r * math.pi)

    def scale(self, k):
        self.r *= k
        print(self.r)

    def is_intersect(self, other):
        print ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2)

circle = Circle(-2,8,5)
circle2 = Circle(9,20,1)
circle.get_area()
circle.scale(5)
circle.get_perimeter()
circle.is_intersect(circle2)


