class ModularTuple(tuple):
    def __new__(cls, iterable=(), size: int = 100):
        iterable = map(lambda item: item % size, iterable)
        return super().__new__(cls, iterable)