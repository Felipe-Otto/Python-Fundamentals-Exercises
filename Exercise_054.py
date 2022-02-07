from datetime import date
total_of_age = total_under_age = 0
for count in range(0, 7):
    year_of_born = int(input('Type the year that the {}° person was born: '.format(count + 1)))
    if date.today().year - year_of_born >= 21:
        total_of_age += 1
    else:
        total_under_age += 1
print('There is {} persons of age.\nThere is {} persons under age.'.format(total_of_age, total_under_age))