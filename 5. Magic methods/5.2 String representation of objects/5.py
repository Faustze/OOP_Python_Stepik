class PhoneNumber:
    def __init__(self, phone_number: str):
        self.pn = ''.join(map(lambda p: p.replace(' ', ''), phone_number))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.pn}')"

    def __str__(self):
        return f"({self.pn[:3]}) {self.pn[3:6]}-{self.pn[6:]}"