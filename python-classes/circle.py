#!/usr/bin/python3
import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self.__radius = value
    
    def area(self):
        return math.pi * self.__radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.__radius
    
    def __str__(self):
        return f"Circle with radius {self.radius} has perimeter {self.perimeter()} and area {self.area()}"
    
circle = Circle(4)
print(circle)

