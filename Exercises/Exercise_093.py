soccer_player = {}
goals = []
soccer_player['name'] = str(input('Type the soccer player name: '))
matches = int(input('Type the quantity of matches played: '))
for count in range(0, matches):
    goals.append(int(input(f'Type the quantity of goals the he did on his {count + 1}° match: ')))
soccer_player['goals'] = goals
soccer_player['total goals'] = sum(goals)
print(f'{"-=" * 30}\n{soccer_player}\n{"-=" * 30}')
for key, value in soccer_player.items():
    print(f'The field {key} has the value {value}.')
print(f'{"-=" * 30}\nThe soccer player {soccer_player["name"]} played {matches} matches:')
for position, value in enumerate(goals):
    print(f'=> On the {position + 1}° match he did {value} goals.')
print(f'Was a total of {soccer_player["total goals"]} goals.')