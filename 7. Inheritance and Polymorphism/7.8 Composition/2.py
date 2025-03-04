class Item:
    def __init__(self, name: str, price: int):
        self.name , self.price = name, price

    def __str__(self):
        return f'{self.name}, {self.price}$'
    

class ShoppingCart:
    def __init__(self, items=()):
        self.items = list(items)

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)
    
    def remove(self, item_name):
        self.items = [item for item in self.items if item_name != item.name]

    def __str__(self):
        return '\n'.join(str(item) for item in self.items)