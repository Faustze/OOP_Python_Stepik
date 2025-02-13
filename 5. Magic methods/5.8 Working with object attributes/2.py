from typing import Any


class Logger:
    def __setattr__(self, old: str, new: str) -> Any:
        print(f'Изменение значения атрибута {old} на {new}')
        self.__dict__[old] = new

    def __delattr__(self, name: str) -> None:
        print(f'Удаление атрибута {name}')
        del self.__dict__[name]