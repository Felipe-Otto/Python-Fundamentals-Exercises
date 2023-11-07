from random import randint
number_of_games = int((input(f'{"-=" *30}\n{"Lottery":^60}\n{"-=" *30}\nType the quantity of games that you wanna play: ')))
numbers_lottery = []
games_lottery = []
print(f'\n{f" Raffling {number_of_games} Lottery Games ":=^60}')
for count1 in range(0, number_of_games):
    for count2 in range(0, 6):
        numbers_lottery.append(randint(1, 60))
    print(f'Lottery game {count1 + 1}: {numbers_lottery}')
    numbers_lottery.clear()
print(f'{" Good Luck ":=^60}')