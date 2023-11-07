from math import hypot
opposite_cathetus = float(input('Type the value of the opposite cathetus: '))
adjacent_cathetus = float(input('Type the value of the adjacent cathetus: '))
print('A triangle with opposite cathetus of {}cm and adjacent cathetus of {}cm has a hypotenuse measuring {:.2f}cm'.format(opposite_cathetus, adjacent_cathetus, hypot(opposite_cathetus, adjacent_cathetus)))