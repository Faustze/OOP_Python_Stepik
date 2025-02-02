class User:
    def __init__(self, name, friends=0):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n

    