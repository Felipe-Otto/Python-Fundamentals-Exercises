def token(name='<unknown>', goals=0):
    print(f'The player {name} made {goals} goal(s) in the championship.')


name = str(input("Type the player's name: "))
goals = str(input('Type the quantity of goals that he made: '))
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
if name.strip() == '':
    token(goals=goals)
else:
    token(name, goals)

