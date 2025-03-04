class Queue:
    def __init__(self, pairs={}):
        self.pairs = {}
        if pairs:
            self.pairs.update(pairs)

    def add(self, elem):
        k, v = elem
        if k in self.pairs:
            del self.pairs[k]
        self.pairs[k] = v

    def pop(self):
        if not self.pairs:
            raise KeyError('Очередь пуста')
        return self.pairs.pop(0)

    def __repr__(self):
        return f'Queue({list(self.pairs.items())})'

    def __len__(self):
        return len(self.pairs)