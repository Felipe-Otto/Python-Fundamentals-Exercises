def write(phrase):
    print(f'{"~" * (len(phrase) + 4)}\n{phrase.title():^{len(phrase) + 4}}\n{"~" * (len(phrase) + 4)}')


while True:
    write(str(input('Type any phrase: ')))
    answer = str(input('Continue [Y, N]: ')).strip().upper()[0]
    while answer not in "YN":
        answer = str(input('Invalid option. Try again! Continue [Y, N]: '))
    if answer == 'N':
        break
