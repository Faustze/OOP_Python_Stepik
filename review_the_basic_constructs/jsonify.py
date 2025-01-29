'''
Реализуйте декоратор @jsonify , преобразующий возвращаемое значение
декорируемой функции в строку формата JSON.
Также декоратор должен сохранять имя и строку документации декорируемой
функции.
'''
import json
from functools import wraps


def jsonify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapper


@jsonify
def get_data():
    """Возвращает данные в виде словаря."""
    return {"name": "Alice", "age": 30}


print(get_data())  # Вывод: {"name": "Alice", "age": 30}
print(get_data.__name__)  # Вывод: get_data
print(get_data.__doc__)   # Вывод: Возвращает данные в виде словаря.
