pharentheses = []
mathematical_expression = str(input('Type an mathematical expression using parentheses: '))
print('Your mathematical expression is right!' if mathematical_expression.count('(') == mathematical_expression.count(')') else 'You mathematical expression is wrong!')




