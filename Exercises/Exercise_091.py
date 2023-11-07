from time import sleep
from random import randint
from operator import itemgetter

dice = {}
ranking = {}
for count in range(1, 5):
    dice[f'Player_{count}'] = randint(1, 6)
    print(f'Player {count + 1} got {dice[f"Player_{count}"]} on the dice.')
    sleep(1)
print(f'{"-=" * 20}\n{"Players Ranking":^40}\n{"-=" * 20}')
ranking = sorted(dice.items(), key=itemgetter(1), reverse=True)
for position, value in enumerate(ranking):
    print(f'{position + 1}° place: {value[0]} with {value[1]} points.')
