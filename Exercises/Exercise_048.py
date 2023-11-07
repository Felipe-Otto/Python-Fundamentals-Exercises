sum_values = total_numbers = 0
for multiple_of_three in range (1, 501, 2):
    if multiple_of_three % 3 == 0:
        sum_values += multiple_of_three
        total_numbers += 1
print('The sum of all {} requested values is {}.'.format(total_numbers, sum_values))