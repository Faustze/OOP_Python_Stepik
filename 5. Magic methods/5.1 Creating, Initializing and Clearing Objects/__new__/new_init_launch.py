class MyClass:
    def __new__(cls, *args, **kwargs):
        print('1. Создание экземпляра класса MyClass')
        instance = super().__new__(cls)
        return instance
    
    def __init__(self):
        print('2. Инициализация созданного экземпляра класса MyClass')
        return None
    
# obj = MyClass.__new__(MyClass)
# MyClass.__init__(obj)
obj = MyClass()

