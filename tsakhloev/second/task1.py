"""
По введеній користувачем даті вивести день тиждня
"""

from re import match

def check_input( day, month, year ):

    if year >= 1 and month <= 12 and month >= 1 and day >= 1:

        if day % 2 == 0:

            if month == 2:  # 2 = 28|29

                if year % 4 == 0 and day <= 28:
                    return True

                elif day <= 29:
                    return True

            elif day <=30:  # 4,6,9,11 = 30
                return True

        elif day <= 31:  # 1,3,5,7,8,10,12 = 31
            return True

    return False

def get_day( day, month, year ):
    weekdays = ['Понеділок', 'Вівторок', 'Середа', 'Четверг', 'П\'ятниця', 'Субота', 'Неділя']

    days = day
    for i in range(month - 1):
        i += 1

        if i % 2 == 0:

            if i == 2:  # 2 = 28|29

                if year % 4 == 0:
                    days += 28

                else:
                    days += 29

            else:  # 4,6,9,11 = 30
                days += 30

        else:  # 1,3,5,7,8,10,12 = 31
            days += 31

    return weekdays[days%7-1]

if __name__ == '__main__':

    date = input('Введіть дату у форматі `31-12-0001`: ') # '10-03-2005'
    match_result = match(r'(\d\d)-(\d\d)-(\d{4})$', date)

    if match_result:

        day, month, year = match_result.groups()
        day, month, year = int(day), int(month), int(year)

        if check_input( day, month, year ):
            print( get_day( day, month, year ) )

        else:
            print('Помилковий ввод')

    else:
        print('Помилковий ввод')

# Можно много всего отрефакторить, но времени нету