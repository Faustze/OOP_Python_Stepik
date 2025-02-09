class FoodInfo:
    def __init__(self, proteins: int | float, fats: int | float, carbohydrates: int | float):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f'{self.__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})'
    
    def __add__(self, value: object):
        if isinstance(value, self.__class__):
            return self.__class__(
                self.proteins + value.proteins, 
                self.fats + value.fats, 
                self.carbohydrates + value.carbohydrates)
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, int | float):
            return self.__class__(
                self.proteins * n, 
                self.fats * n, 
                self.carbohydrates * n)
        return NotImplemented
    
    def __truediv__(self, n):
        if isinstance(n, int | float):
            return self.__class__(
                self.proteins / n, 
                self.fats / n, 
                self.carbohydrates / n)
        return NotImplemented
    
    def __floordiv__(self, n):
        if isinstance(n, int | float):
            return self.__class__(
                self.proteins // n, 
                self.fats // n, 
                self.carbohydrates // n)
        return NotImplemented