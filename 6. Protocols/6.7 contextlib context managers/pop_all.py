"""
Метод pop_all() переносит последовательность обратных вызовов в новый
контекстный менеджер ExitStack и возвращает его.
"""

import contextlib


class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Hello,', self.name)
        return self.name

    def __exit__(self, *args, **kwargs):
        print('Bye,', self.name)
    
def goodbye(name):
    print('Bye,', name)


with contextlib.ExitStack() as stack:
    stack.enter_context(Greeter('Gvido'))
    stack.enter_context(Greeter('Tray'))
    stack.enter_context(Greeter('Alan'))
    new_stack = stack.pop_all()
    print('End the block "with"')