from typing import Iterable


class RandomLooper:
    def __init__(self, *args: Iterable[Iterable]):
        self._args = iter(args)
        self.index = -1
        self._next_element = None

    def __iter__(self):
        for a in self._args:
            yield from a

    def __next__(self):
        try:
            yield from next(self._args)
        except:
            raise StopIteration


randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

answer = [next(randomlooper) for _ in range(4)]
print(answer)