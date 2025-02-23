import contextlib


@contextlib.contextmanager
def nullcontext(enter_result=None):
    """
    Функция nullcontext() используется для построения пустых контекстных
менеджеров, которые ничего не делают. Удобно использовать для создания
необязательного контекстного менеджера.
    """
    yield enter_result


with nullcontext(2077) as manager:
    print(manager)

with nullcontext('pygen') as manager:
    print(manager)