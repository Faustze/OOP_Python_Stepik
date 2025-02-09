class Vector:
    def __init__(self, x: int | float, y: int | float):
        self.x, self.y = x, y

    @property
    def fields(self):
        return self.x, self.y 
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.fields == other
        elif isinstance(other, tuple):
            return self.fields == other
        return NotImplemented