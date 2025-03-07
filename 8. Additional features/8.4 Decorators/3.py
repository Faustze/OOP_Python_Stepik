import functools


class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError('Аргументы должны принадлежать типам int или float')
        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)