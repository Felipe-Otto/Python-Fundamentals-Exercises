distance = int(input('Type the distance of the travel in quilometers: '))
print('You are about to start a trip of {}Km.'.format(distance))
print('The coust of your passage will be ${:.2f}.'.format(distance * 0.5 if distance <= 200 else distance * 0.45))
