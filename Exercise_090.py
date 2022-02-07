student = {}
student['name'] = (str(input("Type the student's name: ")))
student['average'] = float(input("Type the student's average: "))
if student['average'] >= 7:
    student["situation"] = 'approved'
elif 5 <= student['average'] < 7:
    student["situation"] = 'recuperation'
else:
    student["situation"] = 'flunked'
print(f'{"-=" * 20}')
for key, value in student.items():
    print(f"  - The student's {key} is {value}.")
