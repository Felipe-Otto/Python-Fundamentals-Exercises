numbers_list = []
while True:
    numbers_list.append(int(input('Type any integer number: ')))
    answer = str(input('Continue [Y / N]: ')).strip().upper()[0]
    while answer not in 'YN':
        answer = str(input('Invalid option. Try again! Continue [Y / N]: ')).strip().upper()[0]
    if answer == 'N':
        numbers_list.sort(reverse=True)
        break
print(f'{"-=" * 20}\nYou typed {len(numbers_list)} number(s).\nThe typed values in descending order is {numbers_list}.')
print('The number 5 was inserted at the list.' if 5 in numbers_list else "The number 5 wasn't insert at the list.")