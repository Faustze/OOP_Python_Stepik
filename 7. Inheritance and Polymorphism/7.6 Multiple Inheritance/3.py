def get_method_owner(cls, method):
    for c in cls.mro():
        if method in c.__dict__:
            return c