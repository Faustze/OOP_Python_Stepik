from datetime import date, timedelta
from functools import singledispatchmethod


class BirthInfo:
    def __init__(self, birth_date):
        self.birth_date = self.format(birth_date)

    @singledispatchmethod
    def format(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(date)
    def date_format(self, birth_date):
        return birth_date

    @format.register(str)
    def str_format(self, birth_date):
        try:
            return date.fromisoformat(birth_date)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(tuple)
    @format.register(list)
    def list_tuple_format(self, birth_date):
        if len(birth_date) == 3:
            try:
                year, month, day = birth_date
                return date(year, month, day)
            except:
                raise TypeError('Аргумент переданного типа не поддерживается')
        else:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        dt = date.fromordinal((date.today().toordinal() - self.birth_date.toordinal()))
        return dt.year


def current_age(birthday: date, today: date):
    dt = date.fromordinal((today.toordinal() - birthday.toordinal()))
    return dt.year