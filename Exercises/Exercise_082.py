numbers_list = []
even_list = []
odd_list = []
while True:
    number = int(input('Type any integer number: '))
    numbers_list.append(number)
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)
    answer = str(input('Continue [Y / N]: ')). strip().upper()[0]
    while answer not in 'YN':
        answer = str(input('Invalid option. Try again! Continue [Y / N]: ')).strip().upper()[0]
    if answer == 'N':
        break
print(f'{"-=" * 23}\nThe complete list is {numbers_list}\nThe even numbers list is {even_list}\nThe odd numbers list is {odd_list}')
