class SparseArray:
    def __init__(self, default):
        self.default = default
        self.elements = {}

    def __len__(self):
        return len(self.elements)

    def __iter__(self):
        yield from self.elements.values()

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Нужно число типа int')
        return self.elements.get(key, self.default)

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('Введите число типа int')
        self.elements[key] = value