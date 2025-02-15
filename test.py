def sub_generator():
    yield 'a'
    yield 'b'

def main_generator():
    yield from sub_generator()
    yield 'c'

gen = main_generator()

for value in gen:
    print(value)