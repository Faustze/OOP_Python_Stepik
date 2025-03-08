def singleton(cls):
    cls._instance = None

    def wrapper(*args, **kwargs):
        if cls._instance is None:
            cls._instance = cls(*args, **kwargs)

        return cls._instance
    
    return wrapper   