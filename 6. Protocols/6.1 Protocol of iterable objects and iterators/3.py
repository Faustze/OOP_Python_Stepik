from typing import Any


class AttrsIterator:
    def __init__(self, obj: Any):
        self._obj = obj.__dict__.items()

    def __iter__(self):
        for key, value in self._obj:
            yield key, value


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
user = User('Debbie', 'Harry', 77)
attrsiterator = AttrsIterator(user)
print(*attrsiterator)