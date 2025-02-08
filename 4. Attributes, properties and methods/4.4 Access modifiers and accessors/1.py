class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = self.get_diameter
        self._area = self.get_area

    def get_radius(self) -> int:
        return self._radius

    def get_diameter(self) -> int:
        return self._radius * 2
    
    def get_area(self) -> int:
        return __import__("math").pi * self._radius**2
    

circle = Circle(5)
print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))