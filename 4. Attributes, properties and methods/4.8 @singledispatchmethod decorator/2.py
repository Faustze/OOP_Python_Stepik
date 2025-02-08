'''
neg() - метод, принимающий в качестве аргумента объект и возвращающий его 
противоположное значение. Если методу передается целое или вещественное 
число, он должен возвращать это число, взятое спротивоположным знаком. 
Если методу в качестве аргумента передается булево значение, он должен 
возвращать булево значение, противоположное переданному. Если переданный 
объект принадлежит какому-либо другому типу, должно быть возбуждено 
исключение TypeError с текстом: 'Аргумент переданного типа не поддерживается'
'''

from functools import singledispatchmethod
from typing import Any


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(arg: Any):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    def int_float_neg(arg):
        return arg * (-1)

    @neg.register(bool)
    def bool_neg(arg):
        if arg:
            return False
        return True
