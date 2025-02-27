class EasyDict(dict):
    def __getattr__(self, key):
        return super().__getitem__(key)