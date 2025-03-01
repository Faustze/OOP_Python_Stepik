from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name not in instance.__dict__:
            raise AttributeError('Атрибут не найден')
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    @abstractmethod
    def validate(self, value):
        pass


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue, self.maxvalue = minvalue, maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(
                f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
    

class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize, self.maxsize, self.predicate = minsize, maxsize, predicate

    def validate(self, attr):
        if not isinstance(attr, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if self.minsize is not None and len(attr) < self.minsize:
            raise ValueError(
                f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        if self.maxsize is not None and len(attr) > self.maxsize:
            raise ValueError(
                f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        if self.predicate is not None:
            if not self.predicate(attr):
                raise ValueError(
                    'Устанавливаемая строка не удовлетворяет дополнительным условиям')