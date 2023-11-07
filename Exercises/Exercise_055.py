lower_weight = greater_weight = 0
for count in range(0, 5):
    weight = float(input('Type the weight of the {}° person: '.format(count + 1)))
    if count == 1:
        lower_weight = greater_weight = weight
    elif weight < lower_weight:
        lower_weight = weight
    elif weight > greater_weight:
        greater_weight = weight
print('The greater weight typed was {}Kg.\nThe lower weight typed was {}Kg.'.format(greater_weight, lower_weight))