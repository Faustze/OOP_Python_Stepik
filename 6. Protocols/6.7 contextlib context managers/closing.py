import contextlib


@contextlib.contextmanager
def closing(thing):
    """
    Функция closing() используется для построения контекстных менеджеров
из объектов, которые предоставляют метод close() , но не реализуют
протокол контекстного менеджера (отсутствуют
методы __enter__() и __exit__() ).
    """
    try:
        yield thing
    finally:
        thing.close()


class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def close(self):
        print('Пока,', self.name)


with closing(Cat('Кемаль')) as cat:
    print('Привет,', cat)