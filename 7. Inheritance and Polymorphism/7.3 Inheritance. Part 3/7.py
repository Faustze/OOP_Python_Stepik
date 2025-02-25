class AdvancedTuple(tuple):
    def __new__(cls, iterable=None):
        if iterable is None:
            iterable = ()
        return super().__new__(cls, iterable)

    def __add__(self, other):
        if isinstance(other, (tuple, list)):
            return self.__class__(tuple(self) + tuple(other))
        elif isinstance(other, dict):
            return self.__class__(tuple(self) + tuple(other.items()))
        elif isinstance(other, str):
            return self.__class__(tuple(self) + tuple(other))
        elif hasattr(other, '__iter__'):
            return self.__class__(tuple(self) + tuple(other))
        return NotImplemented
    
    def __radd__(self, other):
        if isinstance(other, (tuple, list)):
            return self.__class__(tuple(other) + tuple(self))
        elif isinstance(other, dict):
            return self.__class__(tuple(other.items()) + tuple(self))
        elif isinstance(other, str):
            return self.__class__(tuple(other) + tuple(self))
        elif hasattr(other, '__iter__'):
            return self.__class__(tuple(other) + tuple(self))   
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, (tuple, list)):
            return self.__class__(tuple(self) + tuple(other))
        elif isinstance(other, dict):
            return self.__class__(tuple(self) + tuple(other.items()))
        elif hasattr(other, '__iter__'):
            return self.__class__(tuple(self) + tuple(other))
        elif isinstance(other, str):
            return self.__class__(tuple(self) + tuple(other))
        return NotImplemented