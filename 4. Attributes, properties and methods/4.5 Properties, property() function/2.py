class HourClock:
    def __init__(self, h: int):
        self.hours = h

    @property
    def hours(self):
        return self._hours
    
    @hours.setter
    def hours(self, h):
        if isinstance(h, int) and h in range(1, 12):
            self._hours = h
        else:
            raise ValueError('Некорректное время')
