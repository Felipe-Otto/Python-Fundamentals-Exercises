gender = str(input('Enter your gender [M/F]: ')).strip().upper()
while gender not in 'MF':
    gender = str(input('Invalid data! Please, enter your gender [M/f]: ')).strip().upper()
print('Gender "{}" registered successfully!'.format(gender))
