matrix = [[], [], []]
for count1 in range(0, 3):
    for count2 in range(0, 3):
        matrix[count1].append(int(input(f'Type any integer value for the position [{count1 + 1}, {count2 + 1}]: ')))
total_even_numbers = numbers_sum = 0
print(f'{"-=" * 30}')
for count1 in range(0, 3):
    for count2 in range(0, 3):
        print(f'[{matrix[count1][count2]:^3}]', end=' ')
        if matrix[count1][count2] % 2 == 0:
            total_even_numbers += matrix[count1][count2]
        if count1 == 1:
            if count2 == 0:
                greater_number = matrix[count1][count2]
            elif matrix[count1][count2] > greater_number:
                greater_number = matrix[count1][count2]
        if count2 == 2:
            numbers_sum += matrix[count1][count2]
    print()
print(f'{"-=" * 30}\nThe sum of the even numbers is {total_even_numbers}.\nThe sum of the third numbers column is {numbers_sum}.\nThe greater number of the second line is {greater_number}.')