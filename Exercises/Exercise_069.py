total_person_over_18 = total_mens = young_women = 0
print(f'{"-=" * 9}\n Person  register ')
while True:
    age = int(input(f'{"-=" * 9}\nType the age: '))
    if age > 18:
        total_person_over_18 += 1
    gender = str(input('Type the gender [M / F]: ')).strip().upper()[0]
    if gender == 'M':
        total_mens += 1
    elif gender == 'F' and age < 20:
        young_women += 1
    answer = str(input('Continue [Y / N]: ')).strip().upper()[0]
    while answer not in 'YN':
        answer = str(input('Invalid option. Try again! Continue [Y / N]: ')).strip().upper()[0]
    if answer == 'N':
        break
print(f'{"-=" * 9}\nThe total of persons over 18 years is {total_person_over_18}.\nThe total of registered mens is {total_mens}.\nThe total of women with less than 20 years is {young_women}.')

