from time import sleep


def title():
    print(f'\033[30;42m{"-" * 24}\n{"Help System PyHELP":^24}\n{"-" * 24}')


def access(command):
    space = 34 + len(command)
    print(f'\033[30;44m{"~" * space}\n{f"Accessing the manual of command {command}":^{space}}\n{"~" * space}')
    print('\033[1;107m', end='')
    sleep(1)


def helpFunction(command):
    print(f'\033[7;30m{help(command)}')


while True:
    title()
    command = str(input('\033[0;0mFunction or Library ("END" to exit) > ')).strip()
    if command.upper() == "END":
        break
    access(command)
    helpFunction(command)

print(f'\033[7;31m{"~" * 16}\n{"End of program":^16}\n{"~" * 16}')
