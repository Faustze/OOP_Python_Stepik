import math
from typing import Any


class QuadraticPolynomial:
    def __init__(self, a: Any, b: Any, c: Any):
        self.a, self.b, self.c = a, b, c

    @property
    def x1(self):
        if self.b**2 - 4 * self.a * self.c < 0:
            x1 = None
            return x1
        x1 = (-self.b - math.sqrt(self.b**2 - 4*self.a*self.c)) / (2*self.a)
        return x1

    @property
    def x2(self):
        if self.b**2 - 4*self.a*self.c < 0:
            x2 = None
            return x2
        x2 = (-self.b + math.sqrt(self.b**2 - 4*self.a*self.c)) / (2*self.a)
        return x2

    @property
    def view(self) -> str:
        b, sign_b = abs(self.b), '-' if self.b < 0 else '+'
        c, sign_c = abs(self.c), '-' if self.c < 0 else '+'
        return f'{self.a}x^2 {sign_b} {b}x {sign_c} {c}'

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, coefs: tuple):
        self.a, self.b, self.c = coefs[0], coefs[1], coefs[2]
        return (self.a, self.b, self.c)


polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 3, 1)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)
