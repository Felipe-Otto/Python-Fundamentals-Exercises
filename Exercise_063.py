print('=' * 20 + '\n Fibonacci Sequence\n' + '=' * 20)
terms = int(input('Type the quantity of terms that you wanna see: '))
number1 = number3 = count = 0
number2 = 1
print('{} → {} →'.format(number1, number2), end=' ')
while count < terms - 2:
    number3 = number1 + number2
    print('{}'.format(number3), end=' → ')
    number1 = number2
    number2 = number3
    count += 1
print('End of the program.')
