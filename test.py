import math
from turtle import circle


class ShapeInterface:
    def get_area(self):
        raise NotImplementedError()

    def get_perimeter(self):
        raise NotImplementedError()


# Write your code here.
class Square(ShapeInterface):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length * self.side_length

    def get_perimeter(self):
        return self.side_length * 4


class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = round(math.pi * (self.radius ** 2), 2)
        return area

    def get_perimeter(self):
        perimeter = round(2 * math.pi * self.radius, 2)
        return perimeter

square = Square(2)
square.get_area()

circle = Circle(3)
circle.get_area()
circle.get_perimeter()
