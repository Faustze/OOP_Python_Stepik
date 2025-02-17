class SkipIterator:
    def __init__(self, iterable, n: int):
        self._iterator = iter(iterable) 
        self.n = n  
        self._next_element = None
        self._prepare_next()

    def _prepare_next(self):
        try:
            for _ in range(self.n):
                next(self._iterator)
            self._next_element = next(self._iterator)
        except StopIteration:
            self._next_element = None 

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_element is None:
            raise StopIteration
        current_element = self._next_element
        self._prepare_next()
        return current_element


skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

print(*skipiterator)
