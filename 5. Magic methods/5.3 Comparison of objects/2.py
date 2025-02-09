from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word: str):
        self.word = word

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.word}')"
    
    def __str__(self):
        return self.word.capitalize()
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return len(self.word) == len(value.word)
        return NotImplemented
    
    def __lt__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return len(self.word) < len(value.word)
        return NotImplemented