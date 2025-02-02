'''
    Будем считать вещественным числом последовательность из одной или более
цифр, которая может начинаться с необязательного символа дефиса "-" , а также
содержать на любой позиции одну десятичную точку "." , кроме случая, когда
точка стоит перед символом дефиса
    Реализуйте функцию is_decimal() , которая принимает один аргумент:
        string — строка, содержащая произвольный набор символов
    Функция должна возвращать True , если строка string представляет собой
целое или вещественное число, или False в противном случае.
'''


def is_decimal(s: str) -> bool:
    if s.find('.') < s.find('-'):
        return False
    else:
        try:
            float(s)
            return True
        except ValueError:
            return False

print(is_decimal('100'))   # True
print(is_decimal('199.1')) # True
print(is_decimal('-0.2'))  # True
print(is_decimal('.-95'))  # False
print(is_decimal('-.95'))  # True
print(is_decimal('.10'))   # True
