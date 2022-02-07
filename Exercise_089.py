data = []
students = []
while True:
    data.append(str(input('Type the name: ')))
    data.append(float(input('Type the 1° note: ')))
    data.append(float(input('Type the 2° note: ')))
    students.append(data[:])
    answer = str(input('Continue [Y / N]: ')).strip().upper()[0]
    while answer not in 'YN':
        answer = str(input('Invalid option! Try again! Continue [Y / N]: ')).strip().upper()[0]
    if answer in 'N':
        break
    data.clear()
print(f'{"-=" * 30}\n{"N.":<4}{"Name":<13}{"Average"}\n{"--" * 12}')
for position, count in enumerate(students):
    print(f'{position:<4}{count[0].capitalize():<13}{(count[1] + count[2]) / 2:>4}')
print(f'{"-" * 24}')
while True:
    answer = int(input('Type the student number to see his notes (Type [ 999 ] to stop): '))
    if answer == 999:
        print('Finalizing...\nCome back soon!')
        break
    while answer < 0 or answer > len(students):
        answer = int(input('Invalid option. try again! Type the student number to see his notes (Type [ 999 ] to stop): '))
    print(f"{'-' * 35}\n{students[answer][0].capitalize()}'s notes is {students[answer][1]} and {students[answer][2]}.\n{'-' * 35}")
