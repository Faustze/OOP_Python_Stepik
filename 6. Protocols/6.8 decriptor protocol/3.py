class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self._times = times

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._times:
            if self._attr in obj.__dict__:
                self._times -= 1
                return obj.__dict__[self._attr]
            raise AttributeError('Атрибут не найден')
        raise MaxCallsException('Превышего количество доступных обращений')
    
    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value


class Student:
    name = LimitedTakes(3)

student = Student()
student.name = 'Gwen'

print(student.name)
print(student.name)
print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)