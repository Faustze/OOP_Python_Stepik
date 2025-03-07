import functools


class ignore_exception:
    def __init__(self, *args):
        self.args = args

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
                return value
            except Exception as error:
                if type(error) in self.args:
                    print(f'Исключение {type(error).__name__} обработано')
                    return True
                else:
                    raise
        return wrapper