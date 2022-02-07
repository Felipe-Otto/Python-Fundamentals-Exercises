print(f"""{"-=" * 10}\n{"Ottos's Store":^20} \n{"-=" * 10}""")
total_spend = expensive_products = count = 0
while True:
    product_name = str(input("Type the product's name: ")).capitalize().strip()
    price = float(input("Type the product's value: $"))
    if count == 0:
        cheap_product_price = price
        cheap_product_name = product_name
    elif price < cheap_product_price:
        cheap_product_name = product_name
    total_spend += price
    count += 1
    if price > 1000:
        expensive_products += 1
    answer = str(input('Continue [Y / N]: ')).strip().upper()[0]
    while answer not in 'YN':
        answer = str(input('Invalid option. Try again! Continue [Y / N]: ')).strip().upper()[0]
    if answer == 'N':
        break
    print('-' * 20)
print(f'{"End of the program":-^30}\nThe total spend was ${total_spend}\nThere is {expensive_products} product(s) costing more tha $1000.\nThe cheapest product was the {cheap_product_name} costing ${cheap_product_price}.')
