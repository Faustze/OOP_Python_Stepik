from collections.abc import MutableSequence


class SortedList(MutableSequence):
    def __init__(self, iterable=()):
        self._iterable = sorted(iterable)

    def add(self, obj):
        self._iterable.insert(0, obj)

    def discard(self, obj):
        if obj in self._iterable:
            self._iterable.remove(obj)

    def update(self, iterable):
        self._iterable.extend(iterable)
        self._iterable.sort()

    def __repr__(self):
        return f'{self.__class__.__name__}({str(self._iterable)})'

    def __len__(self):
        return len(self._iterable)

    def __contains__(self, item):
        return item in self._iterable

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._iterable[item]
        return NotImplemented

    def __delitem__(self, item):
        if isinstance(item, (int, slice)):
            del self._iterable[item]
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(sorted(sorted(self._iterable) + sorted(other._iterable)))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, type(self)):
            self._iterable = sorted(
                sorted(self._iterable) + sorted(other._iterable))
            return self
        return NotImplemented

    def __mul__(self, num):
        if isinstance(num, int):
            return type(self)(sorted(sorted(self._iterable) * num))
        return NotImplemented

    def __imul__(self, num):
        if isinstance(num, int):
            self._iterable = sorted(self._iterable * num)
            return self
        return NotImplemented

    def __setitem__(self, index, item):
        raise NotImplementedError

    def insert(self, index, value):
        raise NotImplementedError

    def append(self, value):
        raise NotImplementedError

    def extend(self, values):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError