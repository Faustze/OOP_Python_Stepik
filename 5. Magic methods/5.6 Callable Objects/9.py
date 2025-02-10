class CachedFunction:
    def __init__(self, func):
        self.cache = {}
        self.func = func

    def __call__(self, *args):
        self.cache.setdefault(args, self.func(*args))
        return self.func(*args)