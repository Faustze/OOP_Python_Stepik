class FuzzyString(str):
    def __eq__(self, obj):
        if isinstance(obj, (type(self), str)):
            return self.lower() == obj.lower()
        return NotImplemented
    
    def __ne__(self, obj):
        if isinstance(obj, (type(self), str)):
            return self.lower() != obj.lower()
        return NotImplemented
    
    def __gt__(self, obj):
        if isinstance(obj, (type(self), str)):
            return self.lower() > obj.lower()
        return NotImplemented
    
    def __ge__(self, obj):
        if isinstance(obj, (type(self), str)):
            return self.lower() >= obj.lower()
        return NotImplemented
    
    def __lt__(self, obj):
        if isinstance(obj, (type(self), str)):
            return self.lower() < obj.lower()
        return NotImplemented
    
    def __le__(self, obj):
        if isinstance(obj, (type(self), str)):
            return self.lower() <= obj.lower()
        return NotImplemented   
    
    def __contains__(self, obj) -> bool:
        if isinstance(obj, (type(self), str)):
            return obj.lower() in self.lower()
        return NotImplemented