number1 = int(input('Type an integer value for the first number: '))
number2 = int(input('Type an integer value for the second number: '))
if number1 > number2:
    print('The first number ({}) is bigger than the second number ({}).'.format(number2, number1))
elif number1 < number2:
    print('The first number ({}) is smaller than the number second ({}).'.format(number1, number2))
else:
    print('The two typed numbers has the same value.')