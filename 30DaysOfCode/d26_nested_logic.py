# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import datetime

def get_fine(date_returned, date_expected):
    days = (date_returned - date_expected).days
    months = date_returned.month - date_expected.month

    if days <= 0:
        return 0
    elif date_returned.year == date_expected.year and months == 0:
        return 15*days
    elif date_returned.year == date_expected.year:
        return 500* months
    else:
        return 10000
        

day_returned, month_returned, year_returned = list(map(int, input().split()))
day_expected, month_expected, year_expected = list(map(int, input().split()))

date_returned = datetime(year_returned, month_returned, day_returned)
date_expected = datetime(year_expected, month_expected, day_expected)

fine = get_fine(date_returned, date_expected)
print(fine)
