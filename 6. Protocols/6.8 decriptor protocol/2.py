class NonNegativeInteger:
    def __init__(self, name, default=None):
        self.name, self.default = name, default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self.name not in obj.__dict__ and self.default is None:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__.get(self.name, self.default)
            
    def __set__(self, obj, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Некорректное значение')
        obj.__dict__[self.name] = value