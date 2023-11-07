print('=' * 41 + '\n  10 terms of an Arithmetic Progression\n' + '=' * 41)
first_number = int(input('Type the first number: '))
common_difference = int(input('Type the common difference: '))
for count in range (1, 11):
    print(first_number, end=' → ')
    first_number += common_difference
print('End of the program.')
