def factorialFuncition(number, show=True):
    factorial = 1
    for count in range(number, 0, -1):
        factorial *= count
        if show == True:
            print(f'{count} =' if count == 1 else f'{count} x', end=' ')
    print(factorial)


factorialFuncition(int(input('Type any integer number: ')), True)