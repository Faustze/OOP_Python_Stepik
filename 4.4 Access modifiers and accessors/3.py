class User:
    def __init__(self, name: str, age: int):
        self.set_name(name)
        self.set_age(age)

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str):
        if not isinstance(new_name, str) or not new_name.isalpha() or not new_name:
            raise ValueError('Некорректное имя')
        else:
            self._name = new_name

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int):
        if not isinstance(new_age, int) or new_age not in range(0, 111):
            raise ValueError('Некорректный возраст')
        else:
            self._age = new_age