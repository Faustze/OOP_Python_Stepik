class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title, self.author, self.year = title, author, year

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __str__(self):
        return f"{self.title} ({self.author}, {self.year})"