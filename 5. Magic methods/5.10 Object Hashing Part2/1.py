from typing import Any


class ColoredPoint:
    def __init__(self, x, y, color):
        self.x, self.y, self.color = x, y, color

    @property
    def _fields(self):
        return (self.x, self.y, self.color)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.color})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._fields == other._fields
        return NotImplemented

    def __hash__(self):
        return hash(self._fields)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.__dict__:
            raise AttributeError("You can't modify attrs")
        super().__setattr__(name, value)

