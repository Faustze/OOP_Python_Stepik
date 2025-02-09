from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year: int, month: int):
        self.year, self.month = year, month
   
    def __repr__(self):
        return f"{self.__class__.__name__}({self.year}, {self.month})"
    
    def __str__(self):
        return f"{self.year}-{self.month}"
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return (self.year, self.month) == (value.year, value.month)
        elif isinstance(value, tuple):
            return (self.year, self.month) == value
        return NotImplemented
    
    def __gt__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return (self.year, self.month) > (value.year, value.month)
        elif isinstance(value, tuple):
            return (self.year, self.month) > value
        return NotImplemented