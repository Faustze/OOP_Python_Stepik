from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register
    def list_format(self, ipaddress: list | tuple):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return f"{self.ipaddress}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.ipaddress}')"