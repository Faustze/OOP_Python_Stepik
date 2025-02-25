class SuperInt(int):
    def __new__(cls, value: int):
        return super().__new__(cls, value)
    
    def repeat(self, n: int = 2):
        return self.__class__('-' + str(abs(self)) * n if '-' in str(self) else str(abs(self)) * n)
    
    def to_bin(self) -> str:
        return '-' + bin(abs(self))[2:] if self < 0 else bin(self)[2:]
    def next(self):
        return self.__class__(self + 1)
    
    def prev(self):
        return self.__class__(self - 1)
    
    def __iter__(self):
        yield from map(self.__class__, str(abs(self)))


superint1 = SuperInt(2023)

for item in superint1:
    print(item, type(item))