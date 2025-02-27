from collections import UserList


class DefaultList(UserList):   
    def __init__(self, iterable=(), default=None):
        self.data = list(iterable)
        self._default = default

    def __getitem__(self, index):
        try:
            return self.data[index]
        except IndexError:
            return self._default