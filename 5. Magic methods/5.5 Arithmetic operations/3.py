class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self) -> str:
        return self.string

    def __add__(self, value: object):
        if isinstance(value, self.__class__):
            return self.__class__(self.string + value.string)
        return NotImplemented

    def __mul__(self, value: object):
        if isinstance(value, int):
            return self.__class__(self.string * value)
        return NotImplemented

    def __rmul__(self, value: object):
        return self.__class__(self.__mul__(value))

    def __truediv__(self, value: object):
        if isinstance(value, int):
            return self.__class__(
                self.string[:len(self.string) // value]
            )
        return NotImplemented

    def __lshift__(self, value: object):
        if isinstance(value, int):
            return self.__class__(
                self.string[:len(self.string)-value] if value < len(self.string) else ''
            )
        return NotImplemented

    def __rshift__(self, value: object):
        if isinstance(value, int):
            return self.__class__(
                self.string[value:] if value < len(self.string) else ''
            )
        return NotImplemented