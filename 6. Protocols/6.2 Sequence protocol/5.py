class OrderedSet:
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = set()
        else:
            self.iterable = set(iterable)

    def add(self, obj):
        self.iterable.add(obj)

    def discard(self, obj):
        self.iterable.discard(obj)

    def __len__(self):
        return len(self.iterable)
    
    def __iter__(self):
        yield from self.iterable

    def __contains__(self, item):
        return item in self.iterable
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return list(self.iterable) == list(value.iterable)
        elif isinstance(value, set):
            return self.iterable == value
        return NotImplemented