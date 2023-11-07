from time import sleep
from random import randint


def greaterNumber(numbers):
    print(f'{"-=" * 25}\nAnalysing the entered values...')
    for count in numbers:
        print(count, end=' ')
        sleep(0.25)
    print(f'In the total {len(numbers)} numbers was entered.\nThe greater number entered is {max(numbers)}.')


numbers = []
for count1 in range(0, 5):
    for count2 in range(0, randint(1, 10)):
        numbers.append(randint(1, 10))
    greaterNumber(numbers[:])
    numbers.clear()