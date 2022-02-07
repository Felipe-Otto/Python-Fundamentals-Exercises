from random import choice
student1 = str(input('Type first student name: '))
student2 = str(input('Type second student name: '))
student3 = str(input('Type third student name: '))
student4 = str(input('Type fourth student name: '))
students = [student1, student2, student3, student4]
print('{} was chosen to erase the board.'.format(choice(students)))