height = float(input('Type the height of the wall in meters: '))
width = float(input('Type the width of the wall also in meters: '))
print("A wall with {:.2f} meters of heigth and {:.2f} meters of width has an area of {} m².\nKnowing that one liters of ink it's used in 2m², you'll need {} liters of ink to paint your wall".format(height, width, height * width, (height * width) / 2))