velocity = int(input('Type the current velocity of the car: '))
print('You were fined for exceeding the permitted speed which is 80Km/h!\nYou must pay a fine of ${}.'.format((velocity - 80) * 7) if velocity > 80 else 'Have a good day! Drive with security!')
