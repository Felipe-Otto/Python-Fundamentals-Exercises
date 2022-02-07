tuple_numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'eighteen', 'nineteen', 'twenty')
while True:
    number = int(input('Type any integer number between 0 and 20: '))
    if 0 <= number <= 20:
        break
    print('Invalid option. Try again! ', end='')
print(f'You typed the number {tuple_numbers[number]}.')
