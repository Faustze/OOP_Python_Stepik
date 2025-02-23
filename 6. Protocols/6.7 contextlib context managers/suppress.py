import contextlib


@contextlib.contextmanager
def suppress(*exceptions):
    """
    Функция suppress() используется для построения контекстных
менеджеров, которые игнорируют заданные типы исключений.
    """
    try:
        yield
    except Exception as e:
        if type(e) not in exceptions:
            raise


with suppress(ValueError):
    num = int('python')

print('first test')

with suppress(TypeError, ZeroDivisionError):
    num = 1 / 0

print('second test')