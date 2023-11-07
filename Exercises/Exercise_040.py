note1 = float(input('Type your first note: '))
note2 = float(input('Type your second note: '))
print('Your average is {:.2f}'.format((note1 + note2) / 2))
if (note1 + note2) / 2 < 5:
    print('You were flunked!')
elif ((note1 + note2) / 2) >= 5 and ((note1 + note2) / 2) < 7:
    print('You are in recovery!')
else:
    print('You passed!')