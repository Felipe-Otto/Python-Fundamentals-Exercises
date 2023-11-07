from random import randint
number = randint(0, 10)
attempts = 1
guess = int(input('I just thought of a number between 0 and 10. Try to guess!\nType the number that you think that I thought: '))
while guess != number:
    attempts += 1
    guess = int(input('More... Try again: ' if guess < number else 'Less... Try again: '))
print('You got it on the {}° attempt.'.format(attempts))
