product = float(input("Type the price of the product: "))
print("When applying a 5% discount on US${}, the new price is US${:.2f}.".format(product, product - (product * 0.05)))