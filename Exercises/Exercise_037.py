number = int(input('Type any integer number: '))
choice = int(input('Type [1] to see the conversion of number {} in a binary number.\nType [2] to see the conversion of number {} in a octal number.\nType [3] to see the conversion of number {} in a hexadecimal number.\nChoose one of the above option: '.format(number, number, number)))
if choice == 1:
    print('The number {} converted into a binary number is {}.'.format(number, bin(number)[2:]))
elif choice == 2:
    print('The number {} converted into a octal number is {}.'.format(number, oct(number)[2:]))
elif choice == 3:
    print('The number {} converted into a hexadecimal number is {}.'.format(number, hex(number)[2:]))
else:
    print('Type a valid value!')
