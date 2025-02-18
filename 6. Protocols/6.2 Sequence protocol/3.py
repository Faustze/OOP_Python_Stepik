from itertools import cycle


class CyclicList:
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = []
        else:
            self.iterable = list(iterable)

    def append(self, obj):
        self.iterable.append(obj)

    def pop(self, index=-1):
        return self.iterable.pop(index)
    
    def __len__(self):
        return len(self.iterable)
    
    def __iter__(self):
        yield from cycle(self.iterable)
    
    def __getitem__(self, index):
        return self.iterable[index % len(self.iterable)]
    
    def __setitem__(self, key, value):
        self.iterable[key] = value