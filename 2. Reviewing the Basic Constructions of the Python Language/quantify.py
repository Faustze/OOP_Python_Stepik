'''
Функция quantify() должна считать, для скольких элементов итерируемого
объекта iterable функция-предикат predicate вернула значение True , и
возвращать полученный результат.
'''
from typing import Iterable

def quantify(iterable: Iterable, predicate) -> int:
    if predicate is None:
        predicate = bool
    return sum(map(predicate, iterable))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quantify(numbers, lambda x: x > 1))  # 9

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quantify(numbers, lambda x: x % 2 == 0))  # 5

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quantify(numbers, lambda x: x < 0))  # 0

iterable = ['dddddd', 'a', 'aa', 'aaa', 'bbbb', 'ccccc']
print(quantify(iterable, lambda elem: len(elem) > 3))  # 3

iterable = iter(['cdddddd', 'ca', 'caa', 'caaa', 'cbbbb', 'ccccc', 'c'])
print(quantify(iterable, lambda elem: elem.startswith('c')))  # 7

iterable = iter(['cdddddd', 'ca', 'caa', 'caaa', 'cbbbb', 'ccccc', 'c'])
print(quantify(iterable, lambda elem: elem.endswith('A')))  # 0

iterable = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(quantify(iterable, lambda elem: elem == 1))  # 1

iterable = iter([2, 3, 4, 5, 6, 7, 8, 9, 1])
print(quantify(iterable, lambda elem: elem == 1))  # 1

iterable = iter([2, 3, 4, 1, 5, 6, 7, 8, 9, 10])
print(quantify(iterable, lambda elem: elem == 1))  # 1

iterable = iter(['', 1, 0, (), [[]], [], {1: 2}])  # 3
print(quantify(iterable, None))
