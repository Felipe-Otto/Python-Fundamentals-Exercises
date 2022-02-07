words = ('LEARN', 'PROGRAM', 'LANGUAGE', 'PYTHON', 'COURSE', 'FREE', 'STUDY', 'PRACTICE', 'WORK', 'PROGRAMMER', 'FUTURE', 'MARKET')
for count1 in words:
    print(f'\nIn the word {count1} exists the vowels', end=' ')
    for count2 in count1:
        if count2 in 'AEIOU':
            print(count2.lower(), end=' ')
