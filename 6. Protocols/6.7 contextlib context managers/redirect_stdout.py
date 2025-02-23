"""
Функция redirect_stdout() используется для построения контекстных
менеджеров, которые временно перенаправляют поток sys.stdout в
указанный файлоподобный объект.
"""

from contextlib import redirect_stdout


with open('output.txt', mode='w', encoding='utf-8') as file:
    with redirect_stdout(file):
        help(len)