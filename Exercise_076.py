products = ('Pencil', 1.75, 'Eraser', 2, 'Notebook', 15.9, 'Pencil Case', 25, 'Protractor', 4.2, 'Compass', 9.99, 'Bag', 120.33, 'Pen', 22.30, 'Book', 34.9)
print(f'{"-=" * 20}\n{"Listing of Prices":^40}\n{"-=" * 20}')
for count in range(0, len(products)):
    if count % 2 == 0:
        print(f'{products[count]:.<31}${products[count + 1]:>8.2f}')
print(f'{"-=" * 20}')
