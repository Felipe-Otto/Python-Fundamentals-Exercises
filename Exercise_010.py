#Considering that 1 USD equals 5,44 BRL (01/19/2022, 22:20)
dollar = float(input('Type how many dollar you have: '))
print('You can purchase R${:.2f} with US${}.'.format(dollar * 5.44, dollar))