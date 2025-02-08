from typing import List


class Wordplay:
    def __init__(self, words=()):
        self.words = []
        self.words.extend(words)
        
    def add_word(self, word: str):
        self.words.append(word)
        
    def words_with_length(self, n: int) -> List[str]:
        return [w for w in self.words if len(w) == n]
    
    def only(self, *args: str) -> List[str]:
        return [w for w in self.words if set(w).issubset(set(args))]

    def avoid(self, *args: str) -> List[str]:
        return [w for w in self.words if len(set(w) & set(args)) == 0]
