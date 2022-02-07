from datetime import date
people = {}
people['name'] = str(input("Type the name: "))
people['age'] = (date.today().year - (int(input("Type the year of birth: "))))
people['work card'] = int(input("Type the work card numbers (Type [0] if he don't have it): "))
if people['work card'] != 0:
    people['year of hiring'] = int(input("Type the year of hiring: "))
    people['salary'] = float(input("Type the salary value: "))
    people['retirement'] = people['age'] + ((people['year of hiring'] + 35) - date.today().year)
print(f'{"-=" * 30}')
for key, value in people.items():
    print(f'The {key} is {value}.')