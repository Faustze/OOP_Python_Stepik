from collections import UserString


class MutableString(UserString):
    def lower(self):
        self.data = self.data.lower()
    
    def upper(self):
        self.data = self.data.upper()
    
    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse)) 

    def __setitem__(self, index, value):
        self.data = self.data[:index] + value + self.data[index + 1:]

    def __delitem__(self, index):
        self.data = self.data[:index] + self.data[index + 1:]