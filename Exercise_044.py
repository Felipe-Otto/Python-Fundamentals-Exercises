purchase_amount = float(input('=' * 10 + " Otto's Store " + '=' * 10 + "\nType the purchase amount: $"))
payment = int(input('\nType [ 1 ] for cash/check payment.\nType [ 2 ] for debit card payment.\nType [ 3 ] for 2 installments credit card payment.\nType [ 4 ] for 3 installments or more on credit card.\nForm of payment:'))
if payment == 1:
    print('Applying a 10% discount on {}, the new value to pay is ${}.'.format(purchase_amount, purchase_amount - purchase_amount * 0.1))
elif payment == 2:
    print('Applying a 10% discount on {}, the new value to pay is ${}.'.format(purchase_amount, purchase_amount - purchase_amount * 0.05))
elif payment == 3:
    print("There's no discount to apply in a credit card purchase. The value still {}.".format(purchase_amount))
elif payment == 4:
    installments = int(input("Type the quantity of installments that you want: "))
    print('Your purchase will be paid in {} installments with interest. The new value to pay is ${}.'.format(installments, purchase_amount + purchase_amount * 0.2))
else:
    print('Please choose a valid option!')