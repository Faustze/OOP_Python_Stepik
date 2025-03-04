class Shape:
    __slots__ = ('name', 'color', 'area')

    def __init__(self, name, color, area):
        self.name, self.color, self.area = name, color, area

    def __str__(self):
        return f'{self.color} {self.name} ({self.area})'
    
    def __eq__(self, obj):
        if isinstance(obj, self.__class__):
            return self.area == obj.area
        return NotImplemented
    
    def __ne__(self, obj):
        if isinstance(obj, self.__class__):
            return self.area != obj.area
        return NotImplemented
    
    def __ge__(self, obj):
        if isinstance(obj, self.__class__):
            return self.area > obj.area
        return NotImplemented
    
    def __gt__(self, obj):
        if isinstance(obj, self.__class__):
            return self.area >= obj.area
        return NotImplemented