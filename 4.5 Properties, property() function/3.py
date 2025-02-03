class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return f'{self.name} {self.surname}'

    def set_fullname(self, fullname: str):
        self.name, self.surname = fullname.split()

    fullname = property(fget=get_fullname, fset=set_fullname)
