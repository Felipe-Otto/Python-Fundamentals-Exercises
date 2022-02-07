segment1 = float(input("Type the value of the first segment: "))
segment2 = float(input("Type the value of the second segment: "))
segment3 = float(input("Type the value of the third segment: "))
if segment1 < segment2 + segment3 and segment2 < segment1 + segment3 and segment3 < segment1 + segment2:
    if segment1 == segment2 and segment2 == segment3:
        print('The segments above can form an equilateral triangle.')
    elif segment1 != segment2 and segment1 != segment3 and segment2 != segment3:
        print('The segments above can form a scalene triangle.')
    else:
        print('The segments above can form an isosceles triangle.')
else:
    print("The segments above can't form a triangle!")