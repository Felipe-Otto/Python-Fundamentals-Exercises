from time import sleep
from random import randint
choice = int(input("Let's play Rock-Paper-Scissors!\nEnter [ 1 ] fot Rock\nEnter [ 2 ] for Paper\nEnter [ 3 ] for Scissor\nChoose one of the options above: "))
print('Rock...')
sleep(0.75)
print('Paper...')
sleep(0.75)
print('Scissor...')
sleep(0.75)

if randint(1, 3) == 1 and choice == 3:
    print('-=' * 10 + '\nPlayer: Scissor\nComputer: Rock\n' + '-=' * 10 + '\nComputer wins!')
elif randint(1, 3) == 2 and choice == 1:
    print('-=' * 10 + '\nPlayer: Rock\nComputer: Paper\n' + '-=' * 10 + '\nComputer wins!')
elif randint(1, 3) == 3 and choice == 2:
    print('-=' * 10 + '\nPlayer: Paper\nComputer: Scissor\n' + '-=' * 10 + '\nComputer wins!')
elif randint(1, 3) == 3 and choice == 1:
    print('-=' * 10 + '\nPlayer: Rock\nComputer: Scissor\n' + '-=' * 10 + '\nYou win!')
elif randint(1, 3) == 1 and choice == 2:
    print('-=' * 10 + '\nPlayer: Paper\nComputer: Rock\n' + '-=' * 10 + '\nYou win!')
elif randint(1, 3) == 2 and choice == 3:
    print('-=' * 10 + '\nPlayer: Scissor\nComputer: Paper\n' + '-=' * 10 + '\nYou win!')
elif randint(1, 3) == 1 and choice == 1:
    print('-=' * 10 + '\nPlayer: Rock\nComputer: Rock\n' + '-=' * 10 + "\nIt's a tie!")
elif randint(1, 3) == 2 and choice == 2:
    print('-=' * 10 + '\nPlayer: Paper\nComputer: Paper\n' + '-=' * 10 + "\nIt's a tie!")
elif randint(1, 3) == 3 and choice == 3:
    print('-=' * 10 + '\nPlayer: Scissor\nComputer: Scissor\n' + '-=' * 10 + "\nIt's a tie!")