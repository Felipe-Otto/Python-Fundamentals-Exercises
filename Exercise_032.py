from datetime import date
year = int(input('Type any year that you want to analyse ("0" to analyse current year): '))
if year == 0:
    year = date.today().year
print('{} is a leap year!'.format(year) if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "{} isn't a leap year!".format(year))