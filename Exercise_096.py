def terrainControl(width, length):
    print(f'The area of a terrain with {width} x {length} is {width * length:.2f}m²')


print(f'Terrain Control\n{"-" * 15}')
terrainControl(float(input('Type the width in meters: ')), (float(input('Type the length in meters: '))))
