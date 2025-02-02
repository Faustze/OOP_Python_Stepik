'''
    Целым числом будем считать последовательность из одной или более цифр,
которая может начинаться с необязательного символа дефиса "-".
    Реализуйте функцию is_integer(), которая принимает один аргумент:
string — строка, содержащая произвольный набор символов.
    Функция должна возвращать True , если строка string представляет собой
целое число, или False в противном случае.
'''


def is_integer(s: str) -> bool:
    if not s:
        return False
    
    s = s.lstrip('-')
    return s.isdigit()


print(is_integer('199'))  # True
print(is_integer('-43'))  # True
print(is_integer('5f'))  # False
print(is_integer('5.0'))  # False
print(is_integer('1.1'))  # False
