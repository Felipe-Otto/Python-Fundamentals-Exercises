from datetime import date
year_of_birth = int(input('Type the year that you was born: '))
print("You're {} years old.".format(date.today().year - year_of_birth))
if date.today().year - year_of_birth <= 9:
    print("You're a mirim swimming athlete!")
elif date.today().year - year_of_birth <= 14:
    print("You're a childish swimming athlete!")
elif date.today().year - year_of_birth <= 19:
    print("You're a junior swimming athlete!")
elif date.today().year - year_of_birth <= 25:
    print("You're a senior swimming athlete!")
else:
    print("You're a master swimming athlete!")
