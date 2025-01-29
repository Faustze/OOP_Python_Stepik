'''
    Реализуйте генераторную функцию annual_return(), которая принимает три
аргумента в следующем порядке:
        start — целое число, начальная сумма вклада в рублях.
        percent — целое число, процент, на который текущая сумма вклада будет
увеличиваться каждый год.
        years — целое число, количество лет, в течение которых будут
начисляться проценты.
    Функция должна возвращать итератор, моделирующий банковский вклад.
Возвращаемыми значениями итератора должны являться размеры вклада после
очередного начисления процентов percent.
'''


from typing import Iterator


def annual_return(start: int, percent: int, years: int) -> Iterator[float]:
    deposit = start
    for _ in range(years):
        deposit += deposit * percent/100
        yield deposit


for value in annual_return(120000, 10, 3):
    print(round(value))  # 132000
    # 145200
    # 159720

for value in annual_return(70000, 8, 10):
    print(round(value))  # 75600
# 81648
# 88180
# 95234
# 102853
# 111081
# 119968
# 129565
# 139930
# 151125
