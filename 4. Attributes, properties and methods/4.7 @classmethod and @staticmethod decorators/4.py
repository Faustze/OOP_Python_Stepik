class Pet:
    first, last, count = None, None, 0

    def __init__(self, name: str):
        self.name = name
        if self.__class__.first is None:
            self.__class__.first = self
        self.__class__.count += 1
        self.__class__.last = self

    @classmethod
    def first_pet(cls):
        return cls.first if cls.first is not None else None
        
    @classmethod
    def last_pet(cls):
        return cls.last if cls.last is not None else None

    @classmethod
    def num_of_pets(cls):
        return cls.count