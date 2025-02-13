from typing import Any


class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __getattr__(self, name: str) -> None:
        return self.default

    def __setattr__(self, key, value):
        self.__dict__[key] = value