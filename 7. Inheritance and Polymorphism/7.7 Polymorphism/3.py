from abc import ABC, abstractmethod


class P(ABC):
    def __init__(self, length: int):
        self.length = length
        self.words = []
        self.current_line = []

    def add(self, text):
        for word in text.split():
            if len(' '.join(self.current_line + [word])) > self.length:
                self.words.append(' '.join(self.current_line))
                self.current_line = [word]
            else:
                self.current_line.append(word)

    @abstractmethod
    def end(self):
        pass
    
class LeftParagraph(P):
    def end(self):
        if self.current_line:
            self.words.append(' '.join(self.current_line))
        for line in self.words:
            print(line)
        self.words = []
        self.current_line = []


class RightParagraph(P):
    def end(self):
        if self.current_line:
            self.words.append(' '.join(self.current_line))
        for line in self.words:
            print(line.rjust(self.length))
        self.words = []
        self.current_line = []