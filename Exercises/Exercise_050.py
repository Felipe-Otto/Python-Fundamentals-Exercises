sum = total_numbers = 0
for count in range(1, 7):
    number = int(input('Type the {}° integer number: '.format(count)))
    if number % 2 == 0:
        sum += number
        total_numbers += 1
print('The sum of the {} even numbers typed is {}.'.format(total_numbers, sum))