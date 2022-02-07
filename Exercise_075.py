total_even_numbers = 0
numbers = (int(input('Type the 1° integer number: ')), int(input('Type the 2° integer number: ')), int(input('Type the 3° integer number: ')), int(input('Type the 4° integer number: ')))
print(f'{"-=" * 20}\nThe number 9 was typed {numbers.count(9)} time(s).')
print(f'The number 3 was typed the first time in the {numbers.index(3) + 1}° input.' if 3 in numbers else "The number 3 wasn't typed!")
print('The even numbers typed was:', end=' ')
for count in numbers:
    if count % 2 == 0:
        print(count, end=' ')

