from typing import Any


class NonNegativeObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():  
            setattr(self, k, v)

    def __setattr__(self, name: str, value: Any) -> None:
        if isinstance(name, int | float):
            value = abs(value)
        object.__setattr__(self, name, value)