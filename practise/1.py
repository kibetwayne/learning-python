def print_list(*arg):
    print(f'the list contains: {arg}')
    
print_list('eggs', 'bread', 'peanut butter')

def new(*args):
    print(f'{args} are thw new kids')
new('mathew', 'john')

#!================================================================

#number of days per month, 1st value is a place holder
month_days = [1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    return 29 if month == 2 and is_leap_year(year) else month_days[month]

print(days_in_month(2020, 3))