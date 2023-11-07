from datetime import date
year_of_birth = int(input('Type the year that you was born: '))
print("You'll turn {} in {}.".format(date.today().year - year_of_birth, date.today().year))
if date.today().year - year_of_birth < 18:
    print('Your enlist will take place in {} year(s).\nYour enlist will happen in {}.'.format(18 - (date.today().year - year_of_birth), year_of_birth + 18))
elif date.today().year - year_of_birth == 18:
    print('You must enlist yourself immediately!')
else:
    print('You should have enlisted yourself {} years ago.\nYour enlist happened in {}.'.format((date.today().year - year_of_birth) - 18, year_of_birth + 18))