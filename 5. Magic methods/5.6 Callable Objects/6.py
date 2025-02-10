class Filter:
    def __init__(self, predicate):
        self.predicate = bool if predicate is None else predicate

    def __call__(self, iterable):
        lst = [el for el in iterable if self.predicate(el)]
        return lst