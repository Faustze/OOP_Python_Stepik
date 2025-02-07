from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(arg):
        raise TypeError('Аргумент переданного типа не поддерживается')
        
    @format.register(int)
    def int_format(arg):
        print(f'Целое число: {arg}')
    
    @format.register(float)
    def float_format(arg):
        print(f'Вещественное число: {arg}')
    
    @format.register(list)
    def list_format(arg):
        print('Элементы списка' + ': ' + ', '.join(str(i) for i in arg))
    
    @format.register(tuple)
    def tuple_format(arg):
        print('Элементы кортежа' + ': ' + ', '.join(str(lst) for lst in arg))
    
    @format.register(dict)
    def dict_format(arg):
        print('Пары словаря' + ': ' + ', '.join(str(tpl) for tpl in arg.items()))


Formatter.format(1337)                            # Целое число: 1337
Formatter.format(20.77)                           # Вещественное число: 20.77
Formatter.format([10, 20, 30, 40, 50])            # Элементы списка: 10, 20, 30, 40, 50
Formatter.format(([1, 3], [2, 4, 6]))             # Элементы кортежа: [1, 3], [2, 4, 6]
Formatter.format({'Cuphead': 1, 'Mugman': 3})     # Пары словаря: ('Cuphead', 1), ('Mugman', 3)
Formatter.format({1: 'one', 2: 'two'})            # Пары словаря: (1, 'one'), (2, 'two')
Formatter.format({1: True, 0: False})             # Пары словаря: (1, True), (0, False)

try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)                                    # Аргумент переданного типа не поддерживается

not_supported = [str, type, bool, dict, tuple, list]

for item in not_supported:
    try:
        Formatter.format(item)
    except TypeError as e:
        print(e)                                # Аргумент переданного типа не поддерживается
                                                # Аргумент переданного типа не поддерживается
                                                # Аргумент переданного типа не поддерживается
                                                # Аргумент переданного типа не поддерживается
                                                # Аргумент переданного типа не поддерживается
                                                # Аргумент переданного типа не поддерживается