numbers = [[], []]
for count in range(0, 7):
    number = int(input('Type any integer number: '))
    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)
numbers[0].sort()
numbers[1].sort()
print(f'{"-=" * 30}\nThe even numbers is {numbers[0]}\nThe odd numbers is {numbers[1]}')