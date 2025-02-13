from typing import Any


class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        raise AttributeError('Удаление атрибута невозможно')