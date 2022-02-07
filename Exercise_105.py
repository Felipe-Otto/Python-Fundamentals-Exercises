def notesFunction(notes, situation):
    analytics = {}
    analytics['Total notes'] = notes_quantity
    analytics['Greater note'] = max(notes)
    analytics['Lower note'] = min(notes)
    analytics['Average notes'] = sum(notes)/len(notes)
    if situation == True:
        if analytics['Average notes'] >= 7:
            analytics['situation'] = 'Good'
        elif analytics['Average notes'] >= 5:
            analytics['situation'] = 'Regular'
        else:
            analytics['situation'] = 'Bad'
    return analytics


notes = []
notes_quantity = int(input('Type the quantity of notes that you gonna register: '))
for count in range(0, notes_quantity):
    notes.append(float(input(f'Type the {count + 1}° note: ')))
print(notesFunction(notes, situation=False))
