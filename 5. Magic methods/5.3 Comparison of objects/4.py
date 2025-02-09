from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version: str):
        self._parts = [int(i) for i in version.split('.')]
        self._parts += [0] * (3 - len(self._parts))

    def __repr__(self):
        return f"{self.__class__.__name__}('{'.'.join(map(str, self._parts))}')"
    
    def __str__(self):
        return '.'.join(map(str, self._parts))
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return self._parts == value._parts
        return NotImplemented
    
    def __gt__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return self._parts > value._parts
        return NotImplemented