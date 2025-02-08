class Vector:
    def __init__(self, x: int | float, y: int | float):
        self.x, self.y = x, y

    def __str__(self):
        return f"Вектор на плоскости с координатами ({self.x}, {self.y})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"
    
