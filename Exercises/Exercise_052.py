prime_number = int(input('Type any integer number: '))
sum = 0
for count in range(1, 11):
    if prime_number % count == 0:
        sum +=1
        print('\033[32m{}'.format(count), end=' ')
    else:
        print('\033[31m{}'.format(count), end=' ')
if sum <= 2:
    print('\n\033[mThe number {} is divisible for {} numbers.\nThe number {} is a prime number.'.format(prime_number, sum, prime_number))
else:
    print("\n\033[mThe number {} is divisible for {} numbers.\nThe number {} isn't a prime number.".format(prime_number, sum, prime_number))
