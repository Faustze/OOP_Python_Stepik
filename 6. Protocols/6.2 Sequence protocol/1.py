class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.__class__(self.sequence[~key])
        return self.sequence[~key]
    
    def __iter__(self):
        return iter(reversed(self.sequence))

    def __setitem__(self, key, value):
        self.sequence[~key] = value

    def __delitem__(self, key):
        del self.sequence[~key]

    def __reversed__(self):
        return self.sequence