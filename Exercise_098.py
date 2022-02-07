from time import sleep


def counter(start, end, step):
    print(f"{'-=' * 16}\nCounter from {start} to {end} stepping {step}:")
    if end < start and step > 0:
        step *= -1
    for count in range(start, end, step):
        print(count, end=' ')
        sleep(0.5)
    print('End!')


counter(0, 10, 1)
counter(10, 0, 2)
counter(int(input('Type the first number: ')), int(input('Type the last number: ')), int(input('Type the step: ')))
