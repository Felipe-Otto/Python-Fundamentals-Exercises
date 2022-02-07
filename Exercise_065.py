answer = ''
numbers_average = numbers_quantity = 0
while answer != 'N':
    number = int(input('Type an integer number: '))
    if numbers_quantity == 0:
        lower_number = greater_number = number
    elif number < lower_number:
        lower_number = number
    elif number > greater_number:
        greater_number = number
    numbers_average += number
    numbers_quantity += 1
    answer = str(input('Type a valid value. Continue [Y / N]: ')).upper().strip()[0]
print('You typed {} numbers and their average is {}.\nThe lower typed number is {} and the greater number typed is {}.'.format(numbers_quantity, numbers_average / numbers_quantity, lower_number, greater_number))