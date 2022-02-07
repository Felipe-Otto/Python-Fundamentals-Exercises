print('=' * 41 + '\n  10 terms of an Arithmetic Progression\n' + '=' * 41)
first_number = int(input('Type the first number: '))
common_difference = int(input('Type the common difference: '))
count = 0
while count < 10:
    count += 1
    print('{}'.format(first_number), end=' → ')
    first_number += common_difference
print('End of the program.')