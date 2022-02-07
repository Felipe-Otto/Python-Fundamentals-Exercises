number = int(input('Type any integer number: '))
factorial = number
print('{}! = {}'.format(number, number), end=' ')
while number > 1:
    number -= 1
    factorial *= number
    print('x {}'.format(number), end=' ' if number > 1 else ' = {}.'.format(factorial))
