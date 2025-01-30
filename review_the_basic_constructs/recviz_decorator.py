'''
    Реализуйте декоратор @recviz , который полностью визуализирует выполнение
декорируемой функции, в том числе и рекурсивной. Декоратор должен
отображать все рекурсивные вызовы и возвращаемые значения, полученные при
этих вызовах, причем рекурсивные вызовы, выполняемые в глубину, должны
отделяться друг от друга четырьмя пробелами.
    Очередной вызов декорируемой функции при визуализации должен включать в
себя знак -> , имя декорируемой функции и аргументы, переданные при этом
вызове. Возвращаемое значение при визуализации должно включать в себя
знак <- и непосредственно само возвращаемое значение.
'''


from functools import wraps


def recviz(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        spaces = ' ' * wrapper.level * 4

        args_repr = ', '.join(map(repr, args))
        kwargs_repr = ', '.join(f'{k}={repr(v)}' for k, v in kwargs.items())

        if kwargs:
            print(f'{spaces}-> {func.__name__}({args_repr}, {kwargs_repr})')
        else:
            print(f'{spaces}-> {func.__name__}({args_repr})')
        wrapper.level += 1
        result = func(*args, **kwargs)
        wrapper.level -= 1
        print(f"{spaces}<- {result}")

        return result

    wrapper.level = 0
    return wrapper

# Sample Input 1:
# @recviz
# def add(a, b):
#   return a + b
# add(1, b=2)
# Sample Output 1:
# -> add(1, b=2)
# <- 3

# Sample Input 2:
# @recviz
# def add(a, b, c, d, e):
#   return (a + b + c) * (d + e)
# add('a', b='b', c='c', d=3, e=True)
# Sample Output 2:
# -> add('a', b='b', c='c', d=3, e=True)
# <- 'abcabcabcabc'

# Sample Input 3:
# @recviz
# def fib(n):
# if n <= 2:
# return 1
# else:
# return fib(n - 1) + fib(n - 2)
# fib(4)
# Sample Output 3:
# -> fib(4)
#   -> fib(3)
#       -> fib(2)
#       <- 1
#       -> fib(1)
#       <- 1
#   <- 2
#   -> fib(2)
#   <- 1
# <- 3

# Sample Input 4:
# @recviz
# def fact(n):
# if n == 0:
# return 1
# else:
# return n*fact(n-1)
# fact(5)
# Sample Output 4:
# -> fact(5)
#   -> fact(4)
#       -> fact(3)
#           -> fact(2)
#               -> fact(1)
#                   -> fact(0)
#                   <- 1
#               <- 1
#           <- 2
#       <- 6
#   <- 24
# <- 120
