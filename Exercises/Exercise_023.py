number = int(input('Type any number: '))
print('The number {} has {} unities.\nThe number {} has {} dozens.\nThe number {} has {} hundreds.\nThe number {} has {} thousands.'.format(number, number // 1 % 10, number, number // 10 % 10, number, number // 100 % 10, number, number // 1000 % 10))
