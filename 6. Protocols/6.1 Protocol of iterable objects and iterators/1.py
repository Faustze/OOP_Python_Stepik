class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def _fields(self):
        return self.x, self.y, self.z

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.z})'

    def __iter__(self):
        yield from self._fields