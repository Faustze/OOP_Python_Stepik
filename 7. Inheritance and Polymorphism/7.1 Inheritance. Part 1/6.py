class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, num=1):
        self.value += num

    def dec(self, num=1):
        self.value = max(self.value - num, 0)
    

class NonDecCounter(Counter):
    def dec(self, num=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start)
        self.limit = limit

    def inc(self, num=1):
        self.value = min(self.value + num, self.limit)
