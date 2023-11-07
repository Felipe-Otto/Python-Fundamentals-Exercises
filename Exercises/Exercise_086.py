matrix = [[], [], []]
for count1 in range(0, 3):
    for count12 in range(0, 3):
        matrix[count1].append(int(input(f'Type any integer value for the position [{count1 + 1}, {count12 + 1}]: ')))
for count1 in range (0,3):
    for count2 in range(0, 3):
        print(f'[{matrix[count1][count2]:^3}]', end=' ')
    print()
