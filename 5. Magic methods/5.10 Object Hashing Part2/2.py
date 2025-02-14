from typing import Any


class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @property
    def _fields(self):
        return tuple(self.__dict__.items())
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        raise AttributeError('Установка нового атрибута невозможна')

    def __delattr__(self, name: str) -> None:
        raise AttributeError('Удаление атрибута невозможно')
    
    def __repr__(self):
        return f'''{self.__class__.__name__}({", ".join(f"{k}='{v}'" for k, v in self.__dict__.items())})'''

    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return self._fields == value._fields
        return NotImplemented
    
    def __hash__(self):
        return hash(self._fields)