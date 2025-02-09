class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__str__})"

    def __pos__(self):
        return self.__class__(self.x, self.y)

    def __neg__(self):
        return self.__class__(-self.x, -self.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
