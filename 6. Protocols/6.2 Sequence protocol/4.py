from typing import Iterable


class SequenceZip:
    def __init__(self, *args: Iterable[Iterable | int]):
        self.args = list(zip(*args))

    def __len__(self):
        return len(self.args)
    
    def __iter__(self):
        yield from self.args

    def __getitem__(self, index):
        return self.args[index]
    
    def __setitem__(self, key, value):
        self.args[key] = value