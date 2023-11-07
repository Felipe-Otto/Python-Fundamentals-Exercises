city = str(input("Type the city's name that you was born: ")).strip()
print('This city has the word "New" in his name: {}.'.format(city[:3].upper() == 'NEW'))