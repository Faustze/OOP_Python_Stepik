class Numbers:
    def __init__(self):
        self.numbers = []

    def add_number(self, n: int):
        self.numbers.append(n)

    def get_even(self):
        return [number for number in self.numbers if number % 2 == 0]

    def get_odd(self):
        return [number for number in self.numbers if number % 2 != 0]