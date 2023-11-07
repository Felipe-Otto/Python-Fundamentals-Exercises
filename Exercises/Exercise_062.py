print('=' * 41 + '\n  10 terms of an Arithmetic Progression\n' + '=' * 41)
first_number = int(input('Type the first number: '))
common_difference = int(input('Type the common difference: '))
total_terms = count = 0
answer = 10
while answer != 0:
    while count < answer:
        print('{}'.format(first_number), end=' → ')
        total_terms += 1
        count += 1
        first_number += common_difference
    count = 0
    print('Pause')
    answer = int(input('Type the quantity of terms you want to see more: '))
print('Progression finished with {} terms shown.'.format(total_terms))
