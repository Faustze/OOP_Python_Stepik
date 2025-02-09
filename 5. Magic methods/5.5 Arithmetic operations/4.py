class Time:
    def __init__(self, hours: int, minutes: int):
        self.hours, self.minutes = (hours + minutes // 60) % 24, minutes % 60

    def __str__(self) -> str:
        hours = self.hours if self.hours > 9 else '0' + str(self.hours)
        minutes = self.minutes if self.minutes > 9 else '0' + str(self.minutes)
        return f'{hours}:{minutes}'

    def __add__(self, value: object):
        if isinstance(value, self.__class__):
            hours = self.hours + value.hours
            minutes = self.minutes + value.minutes
            return self.__class__(hours, minutes)
        return NotImplemented

    def __iadd__(self, value: object):
        if isinstance(value, self.__class__):
            self.hours = (self.hours + value.hours) % 24
            self.minutes = self.minutes + value.minutes
            if self.minutes > 59:
                self.minutes = self.minutes % 60
                self.hours = self.hours + 1
            return self
        return NotImplemented