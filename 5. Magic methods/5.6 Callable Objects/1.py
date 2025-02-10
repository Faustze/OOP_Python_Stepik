class Calculator:
    def __call__(self, *args, **kwargs):
        a, b, operation = args
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if operation == '+':
                return a + b
            if operation == '-':
                return a - b
            if operation == '*':
                return a * b
            if operation == '/':
                if b == 0:
                    raise ValueError('Деление на ноль невозможно')
                return a / b
        return NotImplemented