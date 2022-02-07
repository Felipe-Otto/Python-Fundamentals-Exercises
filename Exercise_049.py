number = int(input('Type any value to see his multiplication table: '))
for multiplication in range (0, 11):
    print('{} x {:<2} = {}'.format(number, multiplication, number * multiplication))
