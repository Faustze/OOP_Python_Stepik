'''
    Реализуйте функцию pluck(), которая принимает три аргумента в следующем
порядке:
        data — словарь произвольной вложенности
        path — строка, представляющая собой ключ или последовательность
ключей, перечисленных через точку ".".
        default — произвольный объект, значение по умолчанию; имеет
значение None, если не передан явно.
    Функция должна возвращать значение по ключу path из словаря data.
    Если path представляет собой последовательность ключей,
например, key1.key2 , то возвращаемым значением функции должно быть
значение по ключу key2 из словаря data[key1]. Если указанного ключа или
хотя бы одного ключа из последовательности ключей в словаре нет, функция
должна вернуть значение default
'''


from typing import Any, Dict, Optional


def pluck(data: Dict[str, Any], path: str, default: Optional[Any] = None) -> Any:
    keys = path.split(".")
    current = data

    for key in keys:
        current = current.get(key, default)
        if current is default:
            return default

    return current


d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
print(pluck(d, 'x'))     # 40

d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
print(pluck(d, 'a.b'))   # 5

d = {'a': {'b': {'c': {'d': {'e': 4}}}}}
print(pluck(d, 'a.b.c'))  # {'d': {'e': 4}}
