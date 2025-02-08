class Rectangle:
    def __init__(self, length: int, width: int):
        self.length, self.width = length, width

    def __repr__(self):
        return f"{self.__class__.__name__}({self.length}, {self.width})"