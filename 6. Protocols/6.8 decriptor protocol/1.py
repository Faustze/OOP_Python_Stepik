import keyword


class NonKeyword:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        elif self.name in obj.__dict__:
            return obj.__dict__[self.name]
        else:
            raise AttributeError('Атрибут не найден')
    
    def __set__(self, obj, value):
        if isinstance(value, str) and not keyword.iskeyword(value):
            obj.__dict__[self.name] = value
        elif isinstance(value, (int, float, dict, list, tuple, bool)):
            obj.__dict__[self.name] = value
        else:
            raise ValueError('Некорректное значение')
    
    def __delete__(self, obj):
        del obj.__dict__[self.name]