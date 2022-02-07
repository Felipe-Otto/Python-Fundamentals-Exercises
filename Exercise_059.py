number1 = int(input('Type the first value: '))
number2 = int(input('Type de second value: '))
choose = 0
while choose != 5:
    choose = int(input('=' * 10 + " MENU " + '=' * 10 +'\nEnter [ 1 ] to sum\nEnter [ 2 ] to multiply\nEnter [ 3 ] to see the greater number\nEnter [ 4 ] to type two new values\nEnter [ 5 ] to exit\nChoose one of the above options: '))
    print('-=' * 20)
    if choose == 1:
        print('The sum between {} and {} is {}.'.format(number1, number2, number1 + number2))
    elif choose == 2:
        print('The multiplication between {} and {} is {}.'.format(number1, number2, number1 * number2))
    elif choose == 3:
        print('The number {} is greater than {}.'.format(number1, number2) if number1 > number2 else 'The number {} is greater than {}.'.format(number2, number1))
    elif choose == 4:
        number1 = int(input('Type the first value: '))
        number2 = int(input('Type de second value: '))
    elif choose == 5:
        print('Ending processing...')
    else:
        print('Invalid option! Try again.')
    print('-=' * 20)
print('Process end! Check back often!')

