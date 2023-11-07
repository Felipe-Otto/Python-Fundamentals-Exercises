from random import randint
from time import sleep


def numbersDraw(draw):
    print('Drawing 5 values to the list: ', end='')
    for count in range(0, 5):
        draw.append(randint(0, 10))
        print(draw[count], end=' ')
        sleep(0.25)
    print('Okay!')
    evenNumbersSum(draw)


def evenNumbersSum(draw):
    evenSum = 0
    for count in draw:
        if count % 2 == 0:
            evenSum += count
    print(f'Adding the even numbers of {draw}, we get {evenSum}')


draw = []
numbersDraw(draw)
