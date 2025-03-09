from cmath import sqrt
from itertools import starmap
from operator import add, mul, sub


def check_other_value(func):
    def wrapper(self, other):
        if isinstance(other, self.__class__):
            if len(self.args) != len(other.args):
                raise ValueError('Векторы должны иметь равную длину')
            return func(self, other)
        return NotImplemented
    return wrapper


class Vector:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return str(self.args)

    @check_other_value
    def __add__(self, other):
        return self.__class__(*starmap(add, zip(self.args, other.args)))
    
    @check_other_value
    def __sub__(self, other):
        return self.__class__(*starmap(sub, zip(self.args, other.args)))
    
    @check_other_value
    def __mul__(self, other):
        return sum(starmap(mul, zip(self.args, other.args)))
    
    @check_other_value
    def __eq__(self, other):
        return self.args == other.args
    
    def norm(self):
        return sqrt(sum(value ** 2 for value in self.args))