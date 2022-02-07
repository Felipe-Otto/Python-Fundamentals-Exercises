full_name = input('Type your full name: ').strip().split()
print('Nice to meet you!\nYour first name is {}.\nYour last name is {}.'.format(full_name[0].capitalize().title(), full_name[-1].title()))
