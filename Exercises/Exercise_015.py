period = int(input('How many days was the car rented: '))
distance = float(input('How many kilometers was roded with the car: '))
print('The total to pay is US${:.2f}'.format(60 * period + 0.15 * distance))