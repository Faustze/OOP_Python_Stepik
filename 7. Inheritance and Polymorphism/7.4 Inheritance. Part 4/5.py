from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable=()):
        for item in iterable:
            if not isinstance(item, (int, float)):
                raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().__init__(iterable)
        
    def __add__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError('Элементы для сложения должны быть числами')
        return NumberList(super().__add__(other))
    
    def __iadd__(self, other):
        return super().__iadd__(other)
    
    def append(self, item: (int, float)) -> None:
        if not isinstance(item, (int, float)):
            raise TypeError('Элементы для сложения должны быть числами')
        super().append(item)
    
    def extend(self, other):
        for item in other:
            if not isinstance(item, (int, float)):
                raise TypeError('Элементы для сложения должны быть числами')
        super().extend(other)   

    def insert(self, index, item):
        if not isinstance(item, (int, float)):
            raise TypeError('Элементы для сложения должны быть числами')
        super().insert(index, item)