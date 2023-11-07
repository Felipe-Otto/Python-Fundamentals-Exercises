data = []
people_register = []
greater_weight = lower_weight = 0
while True:
    data.append(str(input(f'{"-=" * 20}\nType the name: ')))
    data.append(float(input(f'Type the weight: ')))
    if len(people_register) == 0:
        greater_weight = lower_weight = data[1]
    else:
        if data[1] > greater_weight:
            greater_weight = data[1]
        if data[1] < lower_weight:
            lower_weight = data[1]
    people_register.append(data[:])
    data.clear()
    answer = str(input('Continue [Y / N]: ')).strip().upper()[0]
    while answer not in 'YN':
        answer = str(input('Invalid option. Try again! Continue [Y / N]: ')).strip().upper()[0]
    if answer in 'N':
        break
print(f'{"-=" * 20}\nThe total of person registered was {len(people_register)}.\nThe greater weight registered was {greater_weight}. Weight of ', end='')
for count in people_register:
    if count[1] == greater_weight:
        print(f'{count[0].capitalize()}..', end=' ')
print(f'\nThe lower weight registered was {lower_weight}. Weight of ', end='')
for count in people_register:
    if count[1] == lower_weight:
        print(f'{count[0].capitalize()}..', end=' ')
