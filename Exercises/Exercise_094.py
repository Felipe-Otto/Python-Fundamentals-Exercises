data = []
people = {}
total_age = 0
while True:
    people['name'] = str(input("Type the person's name: ")).title()
    people['gender'] = str(input('Enter his gender [M / F]: ')).strip().upper()[0]
    while people['gender'] not in 'MF':
        people['gender'] = str(input('Invalid option! Try again! Continue[M / F]: ')).strip().upper()[0]
    people['age'] = int(input('Type the age: '))
    total_age += people['age']
    data.append(people.copy())
    answer = str(input('Continue [Y / N]: ')).strip().upper()[0]
    while answer not in 'YN':
        answer = str(input('Invalid option! Try again! Continue[Y / N]: ')).strip().upper()[0]
    if answer == 'N':
        break
print(f"{'-=' * 30}In the total there is {len(data)} persons registered.\nThe average of the typed ages is {total_age / len(data):.2f}\nThe women's registered was", end=' ')
for count in data:
    if count['gender'] == 'F':
        print(f'{count["name"]}', end=' ')
print(f'\nList of over-average people: ')
for count1 in data:
    if count1['age'] > total_age / len(data):
        for key, value in count1.items():
            print(f'{key} = {value}', end='; ')
        print()
print('End of process...')



