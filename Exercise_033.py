number1 = int(input('Type the first value: '))
number2 = int(input('Type the second value: '))
number3 = int(input('Type the third value: '))
smaller = larger = number1
if number2 < number1 and number2 < number3:
    smaller = number2
if number3 < number1 and number3 < number2:
    smaller = number3
if number2 > number1 and number2 > number3:
    larger = number2
if number3 > number1 and number3 > number2:
    larger = number3
print('The smaller typed number is the {}.\nThe larger typed number is the {}.'.format(smaller, larger))