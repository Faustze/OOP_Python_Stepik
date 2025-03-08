import json


def jsonattr(filename):
    def wrapper(cls):
        with open(filename, mode='r', encoding='utf-8') as file:
            dct = json.load(file)
            for k, v in dct.items():
                setattr(cls, k, v)

        return cls
    
    return wrapper