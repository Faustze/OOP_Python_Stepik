class LowerString(str):
    def __new__(cls, obj=''):
        instance = super().__new__(cls, str(obj).lower())
        return instance 
