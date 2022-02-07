numbers_list = []
numbers = 0
while True:
    number = int(input('Type any integer number: '))
    if number not in numbers_list:
        numbers_list.append(number)
    else:
        print('Duplicated value. Number not inserted!')
    answer = str(input('Continue [Y / N]: ')).strip().upper()[0]
    while answer not in 'YN':
        answer = str(input('Invalid option. Try again! Continue [Y / N]: ')).strip().upper()[0]
    if answer == 'N':
        numbers_list.sort()
        break
print(f'{"-=" * 25}\nYou inserted the numbers {numbers_list}')