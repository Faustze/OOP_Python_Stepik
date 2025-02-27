class ValueDict(dict):
    def key_of(self, value):
        for key, val in self.items():
            if val == value:
                return key
        return None
    
    def keys_of(self, value):
        return (key for key in self.keys() if self[key] == value)