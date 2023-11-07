def readNumber(number):
    while True:
        if number.isnumeric():
            number = int(number)
            return number
            break
        else:
            print(f'\033[1;31mError! Type a valid integer number\033[m')
            number = input('Type any integer number: ')

number = readNumber(input('Type any integer number: '))
print(f'You typed the number {number}')