class AttrDict:
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
        self.data[key] = value
        self.__dict__.update({key: value})