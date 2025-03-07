import functools


class reverse_args:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        args = args[::-1]
        value = self.func(*args, **kwargs)
        return value