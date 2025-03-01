from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=()):
        self._iterable = list(iterable)

    def __str__(self):
        return str(self._iterable)
        
    def __len__(self):
        return len(self._iterable)
    
    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._iterable[item]
        return NotImplemented
    
    def __invert__(self):
        return type(self)(int(not item) for item in self._iterable)

    def __or__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self_item | other_item for self_item, other_item in zip(self._iterable, other._iterable))
        return NotImplemented

    def __and__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self_item & other_item for self_item, other_item in zip(self._iterable, other._iterable))
        return NotImplemented

    
bitarray = BitArray([1, 0, 1, 1])
print(bitarray)
print(~bitarray)
print(bitarray[0])
print(bitarray[1])
print(bitarray[-1])
print(0 in bitarray)
print(1 not in bitarray)