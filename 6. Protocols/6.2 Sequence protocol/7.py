class PermaDict:
    def __init__(self, data=None):
        if data is None:
            self.data = {}
        else:
            self.data = data
            self.__dict__.update(data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data

    def __getitem__(self, key):
        return self.data.get(key)

    def __setitem__(self, key, value):
        if key in self.__dict__:
            raise TypeError('Изменение значения по ключу невозможно')
        self.data[key] = value
        self.__dict__.update({key: value})

    def __delitem__(self, key):
        del self.data[key]
        del self.__dict__[key]

    def keys(self):
        return self.data.keys()
    
    def values(self):
        return self.data.values()
    
    def items(self):
        return self.data.items()