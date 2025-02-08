from functools import singledispatchmethod
from typing import Any


class Processor:
    @singledispatchmethod
    @staticmethod
    def process(arg: Any):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(str)
    def str_process(arg):
        return arg.upper()

    @process.register(int)
    @process.register(float)
    def int_float_process(arg):
        return arg * 2

    @process.register(tuple)
    def tuple_process(arg):
        return tuple(sorted(arg))

    @process.register(list)
    def list_process(arg):
        return sorted(arg)
