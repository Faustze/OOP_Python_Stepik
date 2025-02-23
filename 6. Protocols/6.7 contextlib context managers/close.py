"""
Метод close() менеджера ExitStack немедленно опустошает
последовательность обратных вызовов, вызывая с конца все имеющиеся в
нем методы __exit__() и функции.
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
    stack.push(Greeter('Tray'))
    stack.callback(goodbye, 'Alan')
    stack.close()
    print('End the block "with"')