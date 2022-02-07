soccer_player = dict()
soccer_players = []
goals = []
while True:
    soccer_player['Name'] = str(input('Type the soccer player name: '))
    matches = int(input('Type the quantity of matches played: '))
    for count in range(0, matches):
        goals.append(int(input(f'Type the quantity of goals that he did on his {count + 1}° match: ')))
    soccer_player['Goals'] = goals[:]
    soccer_player['Total goals'] = sum(goals)
    soccer_players.append(soccer_player.copy())
    goals.clear()
    answer = str(input('Continue [Y / N]: ')).strip().upper()[0]
    while answer not in 'YN':
        answer = str(input('Invalid option. Try again! Continue [Y / N]: '))
    if answer == 'N':
        break
print(f'{"-=" * 23}\n{"Cod":<5}', end='')
for value in soccer_player.keys():
    print(f'{value:<15}', end='')
print(f'\n{"-" * 46}')
for position, value in enumerate(soccer_players):
    print(f'{position:<5}', end='')
    for count in value.values():
        print(f'{str(count):<15}', end='')
    print()
while True:
    print('-' * 46)
    index = int(input('Type the a soccer player index (Enter [ 999 ] to exit): '))
    if index == 999:
        break
    while index < 0 or index > len(soccer_players):
        index = int(input('Invalid option. Try again! Type the a soccer player index (Enter [ 999 ] to exit): '))
    print(f'-- Soccer player {soccer_players[index]["Name"]}:')
    for position, value in enumerate(soccer_player['Goals']):
        print(f'  On the {position}° game did {value} goals')
print('End of the program. Come back soon!')