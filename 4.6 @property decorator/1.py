class Person:
    def __init__(self, name: str, surname: str):
        self._name, self._surname = name, surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, fullname: str):
        self.name, self.surname = fullname.split()


person = Person('Mike', 'Pondsmith')
person.fullname = 'Troy Baker'
print(person.name)
print(person.surname)