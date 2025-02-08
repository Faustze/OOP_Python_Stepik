import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius 
        self.area = math.pi * self.radius ** 2

