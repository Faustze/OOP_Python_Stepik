class ElectricCar:
    def __del__(self):
        print('Вызов метода __del__()')


cars = [ElectricCar(), ElectricCar()]
del cars
print('Завершение работы')
