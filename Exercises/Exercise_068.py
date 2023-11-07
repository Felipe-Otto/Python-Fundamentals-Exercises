from random import randint
print(f'{"-=" * 8}\n  Even or Odd \n{"-=" * 8}')
wins = 0
while True:
    value1 = int(input('Type any integer value: '))
    choose = str(input('Even or Odd [E / O]: ')).strip().upper()[0]
    while choose != 'E' and choose != 'O':
        choose = str(input('Invalid value. Try again! Even or Odd [E / O]: ')).strip().upper()[0]
    print(f'{"-=" * 8}\nYou played {value1} and the computer played {randint(0, 10)}. The sum between them ({value1 + randint(0, 10)}) is even.\n{"-=" * 8}' if (value1 + randint(0, 10)) % 2 == 0 else f'{"-=" * 8}\nYou played {value1} and the computer played {randint(0, 10)}. The sum between them ({value1 + randint(0, 10)}) is odd.\n{"-=" * 8}')
    if (choose == 'E' and (value1 + randint(0, 10)) % 2 != 0) or (choose == 'O' and (value1 + randint(0, 10)) % 2 != 1):
        print(f'You loose!\nGame over! You won a total of {wins} times.')
        break
    else:
        print(f"You won!\nLet's play again...\n{'-=' * 8}")
        wins += 1
