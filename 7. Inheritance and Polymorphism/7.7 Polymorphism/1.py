from abc import ABC, abstractmethod
from datetime import date


class DateFormat(ABC):
    def __init__(self, year, month, day):
        self._date = date(year, month, day)

    def iso_format(self):
        return self._date.isoformat()

    @abstractmethod
    def format(self):
        pass


class USADate(DateFormat):
    def format(self):
        return self._date.strftime('%m-%d-%Y')


class ItalianDate(DateFormat):
    def format(self):
        return self._date.strftime('%d/%m/%Y')
