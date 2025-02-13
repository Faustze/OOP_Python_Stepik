from typing import Any


class Ord:
    def __setattr__(self, name: str, value: Any) -> None:
        object.__setattr__(self, name, ord(name))

    def __getattribute__(self, name: str) -> Any:
        return object.__getattribute__(self, name)
    
    def __getattr__(self, name: str) -> Any:
        return ord(name)