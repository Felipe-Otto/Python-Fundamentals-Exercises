full_name = str(input('Type your full name: ')).strip()
name_components = full_name.split()
print('Your name in upper case is: {}.\nYour name in lower case is: {}.\nYour full name has a total of {} letters.\nYour first name is {} and it has {} letters.'.format(full_name.upper(), full_name.lower(), len(full_name) - full_name.count(' '), name_components[0],len(name_components[0])))

