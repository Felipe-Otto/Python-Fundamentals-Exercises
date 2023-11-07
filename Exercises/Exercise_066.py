numbers_sum = numbers_quantity = 0
while True:
    number = int(input('Type any integer number (Enter [ 999 ] to stop): '))
    if number == 999:
        break
    numbers_sum += number
    numbers_quantity += 1
print(f'{numbers_quantity} numbers was typed and their sum is {numbers_sum}!')
