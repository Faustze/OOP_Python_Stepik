class ReversibleString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string
    
    def __neg__(self):
        return self.__class__(self.string[::-1])