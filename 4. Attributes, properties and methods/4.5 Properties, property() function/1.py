class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    @property 
    def perimeter(self):
        return 2 * (self.length + self.width) 
    
    @property 
    def area(self):
        return self.length * self.width
    
rectangle = Rectangle(4, 5)
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)
