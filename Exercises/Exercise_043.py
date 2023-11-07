weight = float(input('Type your weight in kilograms: '))
height = float(input('Type your height in meters: '))
print('Your Body Mass Index (BMI) is {:.1f}.'.format(weight / (height ** 2)))
if weight / height ** 2 <= 18.5:
    print("You're underweight!")
elif 18.5 < weight / height ** 2 <= 25:
    print("You're in your normal weight!")
elif 25 < weight / height ** 2 <= 30:
    print("You're overweight!")
elif 30 < weight / height ** 2 <= 40:
    print("You're with obesity!")
else:
    print("You're with morbid obesity!")
