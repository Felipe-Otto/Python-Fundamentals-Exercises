from random import randint
from time import sleep
print('-=' * 30 + "\n I'm gonna think in a number between 0 and 5. Try to guess...\n" + '-=' * 30)
number = randint(0, 5)
guess = int(input('Type the number you think that I thought: '))
print('Processing...')
sleep(3)
print('I won! I thought in the number {} not in the {}!'.format(number, guess) if number != guess else 'Congratulations! You won from me.')