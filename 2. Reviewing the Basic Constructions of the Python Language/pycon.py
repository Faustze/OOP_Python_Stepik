'''
Каждый месяц в Сан-Диего организовывается встреча любителей Python, которая
проходит в четвертый четверг месяца.
>> Формат входных данных <<
На вход программе подается два натуральных числа, представляющие год и
месяц, каждое на отдельной строке.
>> Формат выходных данных << 
Программа должна определить день проведения встречи в Сан-Диего в
указанных году и месяце и вывести результат в формате DD.MM.YYYY
'''
import datetime


def pycon(year: int, month: int) -> str:
    first_day = datetime.date(year, month, 1)
    first_thursday = first_day + \
        datetime.timedelta(days=(3 - first_day.weekday() + 7) % 7)
    fourth_thursday = first_thursday + datetime.timedelta(days=21)

    return fourth_thursday.strftime('%d.%m.%Y')


print(pycon(2012, 3))  # 22.03.2012
print(pycon(2015, 2))  # 26.02.2015
print(pycon(2018, 6))  # 28.06.2018


'''
# Не оптимизированное решение ;/
def pycon(year: int, month: int) -> str:
    cnt_thursdays = 0
    start_day = datetime.date(year=year, month=month, day=1)

    if month == 12:
        last_day = datetime.date(year=year, month=1, day=1) - datetime.timedelta(days=1)
    else:
        last_day = datetime.date(year=year, month=month+1, day=1) - datetime.timedelta(days=1)

    for day in range(start_day.toordinal(), last_day.toordinal() + 1):
        if datetime.date.fromordinal(day).isoweekday() == 4:
            cnt_thursdays += 1
            if cnt_thursdays == 4:
                day = datetime.date.fromordinal(day)
                day = day.strftime('%d.%m.%Y')
                break
    return day
'''
