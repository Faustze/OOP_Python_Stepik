class Vector:
    def __init__(self, x: int | float, y: int | float):
        self.x, self.y = x, y

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __add__(self, value: object):
        if isinstance(value, self.__class__):
            return self.__class__(self.x + value.x, self.y + value.y)
        return NotImplemented

    def __sub__(self, value: object):
        if isinstance(value, self.__class__):
            return self.__class__(self.x - value.x, self.y - value.y)
        return NotImplemented
    
    def __mul__(self, value: object):
        if isinstance(value, int | float):
            return self.__class__(self.x * value, self.y * value)
        return NotImplemented
    
    def __rmul__(self, value: object):
        if isinstance(value, int | float):
            return self.__mul__(value)
        return NotImplemented
    
    def __truediv__(self, value: object):
        if isinstance(value, int | float):
            return self.__class__(self.x / value, self.y / value)
        return NotImplemented