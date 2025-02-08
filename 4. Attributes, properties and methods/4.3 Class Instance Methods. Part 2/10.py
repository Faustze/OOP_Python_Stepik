from typing import List


class TextHandler:
    def __init__(self):
        self.s = []
        self.shortest_word_len = 0
        self.longest_word_len = 0

    def add_words(self, words: str):
        words = words.split()
        self.s.extend(words)
        self.shortest_word_len = min(map(len, self.s))
        self.longest_word_len = max(map(len, self.s))


    def get_shortest_words(self) -> List[str]:
        return [word for word in self.s if len(word) == self.shortest_word_len]
    
    def get_longest_words(self) -> List[str]:
        return [word for word in self.s if len(word) == self.longest_word_len]
