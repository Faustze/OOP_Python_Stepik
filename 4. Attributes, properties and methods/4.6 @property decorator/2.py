import hashlib


class Account:
    def __init__(self, login: str, password: str):
        self._login, self.password = login, password

    def hash_function(self, password: str) -> str:
        hash_object = hashlib.sha256(password.encode())
        return hash_object.hexdigest()

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        raise AttributeError('Изменение логина невозможно')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = self.hash_function(password)
