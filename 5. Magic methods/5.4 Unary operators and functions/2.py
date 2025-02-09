class Money:
    def __init__(self, amount: int):
        self.amount = amount

    def __str__(self):
        return f"{self.amount} руб."
    
    def __pos__(self):
        return self.__class__(abs(self.amount))

    def __neg__(self):
        return self.__class__(-abs(self.amount))