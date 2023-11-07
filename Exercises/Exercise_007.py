student_name = input("Type the student's first name: ")
note1 = float(input("Type {}'s first note: ".format(student_name)))
note2 = float(input("Type {}'s second note: ".format(student_name)))
print("{}'s average is {:.1f}".format(student_name, (note1 + note2) / 2))
