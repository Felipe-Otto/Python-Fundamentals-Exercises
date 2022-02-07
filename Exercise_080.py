greater_number = lower_number = 0
numbers_list = []
for count1 in range(0, 5):
    number = int(input('Type any integer number: '))
    if count1 == 0 or count1 > numbers_list[- 1]:
        numbers_list.append(number)
        print('Number inserted in the end of the list')
    else:
        position = 0
        while position < len(numbers_list):
            if number <= numbers_list[position]:
                numbers_list.insert(position, number)
                print(f'Number inserted in {position + 1}° position.')
                break
            position += 1
print(f'{"-=" * 20}\nThe values inserted was {numbers_list} ')
