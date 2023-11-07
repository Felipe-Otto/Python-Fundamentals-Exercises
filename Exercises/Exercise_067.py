while True:
    number = int(input('Type any number (Enter any negative value to stop process): '))
    print('-=' * 20)
    if number < 0:
        break
    for count in range(0, 11):
        print(f'{number} x {count:<2} = {number * count}')
    print('-=' * 20)
print('Multiplication table program finalized. check back often!')
