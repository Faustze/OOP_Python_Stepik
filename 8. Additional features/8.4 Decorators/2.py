import functools


class MaxCallsException(Exception):
    pass

class limited_calls:
    def __init__(self, n):
        self.n = n
        self.call_count = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.call_count >= self.n:
                raise MaxCallsException('Превышено допустимое количество вызовов')
            self.call_count += 1
            return func(*args, **kwargs)
        return wrapper