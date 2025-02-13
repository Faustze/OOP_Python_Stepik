from typing import Any


class Item:
    def __init__(self, name: str, price: int, quantity: int):
        self.name, self.price, self.quantity = name, price, quantity

    def __getattribute__(self, name: str) -> Any:
        if name == 'name':
            return self.__dict__[name].title()
        return object.__getattribute__(self, name)
    
    def __getattr__(self, name: str) -> Any:
        if name == 'total':
            return self.price * self.quantity