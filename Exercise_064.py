numbers_sum = numbers_quantity = number = 0
while number != 999:
    numbers_sum += number
    numbers_quantity += 1
    number = int(input('Type any integer number (Enter [ 999 ] to stop): '))
print('You typed {} numbers and the sum between them is {}.'.format(numbers_quantity, numbers_sum))
