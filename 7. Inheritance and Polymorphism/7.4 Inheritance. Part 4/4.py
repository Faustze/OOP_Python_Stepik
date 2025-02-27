class AdvancedList(list): 
    def join(self, separator=' '):
        return separator.join(str(el) for el in self)
    
    def map(self, func):
        for item in range(len(self)):
            self[item] = func(self[item])
    
    def filter(self, func):
        for item in self:
            if not func(item):
                self.remove(item)