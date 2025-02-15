from typing import Any


class AttrsIterator:
    def __init__(self, obj: Any):
        self._obj = iter(obj.__dict__.items())

    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self._obj)