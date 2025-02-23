"""
Метод push() менеджера ExitStack принимает в качестве аргумента
контекстный менеджер и добавляет его метод __exit__() в конец
последовательности обратных вызовов, но не вызывает.
"""

import contextlib


class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Привет,', self.name)

    def __exit__(self, *args, **kwargs):
        print('Пока,', self.name)


with contextlib.ExitStack() as stack:
    stack.push(Greeter('Gvido'))
    stack.push(Greeter('Tray'))
    print('End the block "with"')