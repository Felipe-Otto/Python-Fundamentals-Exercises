numbers = []
for count in range(0, 5):
    numbers.append(int(input(f'Type a value for the {count + 1}° position: ')))
print(f'{"-=" * 20}\nYou inserted the numbers {numbers}.\nThe lower number typed was the {min(numbers)} in the position(s):', end=' ')
if numbers.count(min(numbers)) > 1:
    for position, count in enumerate(numbers):
        if min(numbers) == count:
            print(position, end='... ')
    print()
else:
    print(f'{(numbers.index(min(numbers)))}')
print(f'The greater number typed was the {max(numbers)} in the position(s):', end=' ')
if numbers.count(max(numbers)) > 1:
    for position, count in enumerate(numbers):
        if count == max(numbers):
            print(position, end='... ')
else:
    print(f'{numbers.index(max(numbers))}')

