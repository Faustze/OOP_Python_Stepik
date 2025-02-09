class ColoredPoint:
    def __init__(self, x: int, y: int, color: tuple = (0, 0, 0)):
        self.x, self.y = x, y
        self.color = color

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.color})'

    def __pos__(self):
        return self.__class__(self.x, self.y, self.color)

    def __neg__(self):
        return self.__class__(-self.x, -self.y, self.color)

    def __invert__(self):
        r, g, b = self.color
        return self.__class__(self.y, self.x,
                              (255-r, 255-g, 255-b))