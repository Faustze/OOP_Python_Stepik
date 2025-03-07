import functools
from typing import Any


class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs) -> Any:
        try:
            return (self.func(*args, **kwargs), None)
        except Exception as error:
            return (None, type(error))