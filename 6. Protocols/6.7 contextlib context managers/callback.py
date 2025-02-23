"""
Метод callback() менеджера ExitStack принимает в качестве аргумента
функцию, любой набор из позиционных или именованных аргументов для
этой функции, и добавляет эту функцию в конец последовательности
обратных вызовов, но не вызывает.
"""

import contextlib


def goodbye(name):
    print('Bye,', name)


with contextlib.ExitStack() as stack:
    stack.callback(goodbye, 'Gvido')
    stack.callback(goodbye, name='Tray')
    print('End the block "with"')