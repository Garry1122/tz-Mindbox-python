import math 
from abc import ABC, abstractmethod

PI = math.pi 

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @staticmethod
    def is_right_triangle(a, b, c):
        sides = sorted([a, b, c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

def compute_area(shape):
    if isinstance(shape, Shape):
        return shape.area()
    raise TypeError("Неправильная фигура")

# Пример 
circle = Circle(16)
triangle = Triangle(3, 4, 5)

print(f"Площадь круга: {compute_area(circle)}")
print(f"Площадь треугольника: {compute_area(triangle)}")
print(f"Является ли треугольник прямоугольным: {Triangle.is_right_triangle(3, 4, 5)}")