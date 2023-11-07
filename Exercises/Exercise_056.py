average_age = older_man_age = total_younger_woman = 0
for count in range(0, 4):
    print('=' * 5 + ' {}° Person '.format(count + 1) + '=' * 5)
    name = str(input('Type the name: '))
    age = int(input('Type the age: '))
    gender = str(input('Type the gender [M/F]: ')).strip().upper()
    if gender == 'M' and age > older_man:
        older_man_age = age
        older_man_name = name
    elif gender == 'F' and age < 20:
        total_younger_woman += 1
    average_age += age
print('=' * 21 + '\nThe average age of the persons typed is {:.2f} years.\nThe oldest man has {} years and his name is {}.\nThe total of womans that has less than 20 years is {}.'.format(average_age / 4, older_man_age, older_man_name, total_younger_woman))