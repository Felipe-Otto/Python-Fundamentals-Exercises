from random import shuffle
student1 = str(input('Type first student name: '))
student2 = str(input('Type second student name: '))
student3 = str(input('Type third student name: '))
student4 = str(input('Type fourth student name: '))
students = [student1, student2, student3, student4]
shuffle(students)
print('The order of presentation is: \n1° {}\n2° {}\n3° {}\n4° {}'.format(students[0], students[1], students[2], students[3]))