import functools


class type_check:
    def __init__(self, types: list):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg, type in zip(args, self.types):
                if not isinstance(arg, type):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper