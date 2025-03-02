from abc import ABC, abstractmethod
import statistics


class Stats(ABC):
    def __init__(self, iterable=()):
        self._iterable = list(iterable)

    @abstractmethod
    def result(self):
        pass
    
    def add(self, num):
        self._iterable.append(num)

    def clear(self):
        self._iterable.clear()

class MinStat(Stats):
    def result(self):
        return min(self._iterable, default=None)


class MaxStat(Stats):
    def result(self):
        return max(self._iterable, default=None)

    
class AverageStat(Stats):
    def result(self):
        if self._iterable:
            return sum(self._iterable) / len(self._iterable)