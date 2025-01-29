'''
    Реализуйте генераторную функцию intersperse(), которая принимает два
аргумента в следующем порядке:
        iterable — итерируемый объект
        delimiter — значение-разделитель
    Функция должна возвращать генератор, порождающий последовательность из
элементов итерируемого объекта iterable, между которыми располагается
значение-разделитель delimiter.
'''


from typing import Iterable


def intersperse(iterable: Iterable, delimiter: str | int):
    it = iter(iterable)
    try:
        first = next(it)
    except StopIteration:
        return
    
    yield first
    for i in it:
        yield delimiter
        yield i


print(*intersperse([1, 2, 3], 0))   # 1 0 2 0 3
inter = intersperse('beegeek', '!')
print(next(inter))                  # b
print(next(inter))                  # !
print(*inter)                       # e ! e ! g ! e ! e ! k
print(*intersperse('A', '...'))     # A
