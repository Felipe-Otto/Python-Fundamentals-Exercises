phrase = str(input('Type any phrase: ')).strip().split()
palindrome_off = ''.join(phrase)
palindrome_on = ''
for count in range(len(palindrome_off) - 1, -1, -1):
    palindrome_on += palindrome_off[count]
print('The inverse of {} is {}.'.format(palindrome_off.upper(), palindrome_on.upper()))
print('The typed phrase is a palindrome.' if palindrome_on == palindrome_off else "The typed phrase isn't a palindrome.")
