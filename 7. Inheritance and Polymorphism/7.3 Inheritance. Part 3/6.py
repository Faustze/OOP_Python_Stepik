class RoundedInt(int):
    def __new__(cls, num: int | float, even: bool = True):
        num += (num % 2 == 1) if even else (num % 2 == 0)
        instance = super().__new__(cls, num)
        return instance