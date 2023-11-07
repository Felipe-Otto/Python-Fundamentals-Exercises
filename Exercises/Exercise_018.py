from math import radians, sin, cos, tan
angle = float(input('Type any angle: '))
print('The sine of {}° is {:.2f}\nThe cosine of {}° is {:.2f}\nThe tangent of {}° is {:.2f}'.format(angle, sin(radians(angle)), angle, cos(radians(angle)), angle, tan(radians(angle))))