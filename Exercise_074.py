from random import randint
numbers = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('The selected numbers was', end=' ')
for count in numbers:
    print(f'{count}', end=' ')
print(f'\nThe grater number is {max(numbers)}.\nThe lower number is {min(numbers)}.')
