print(f"""{"-=" * 20}\n{"Otto's Bank":^40}\n{"-=" * 20}""")
withdraw = int(input('Type the value that you wanna withdraw: $'))
money_note = 100
total_money_note = 0
while True:
    if withdraw >= money_note:
        withdraw -= money_note
        total_money_note += 1
    else:
        if total_money_note > 0:
            print(f'There is a total of {total_money_note} notes of ${money_note}.')
        if money_note == 100:
            money_note = 50
        elif money_note == 50:
            money_note = 20
        elif money_note == 20:
            money_note = 10
        elif money_note == 10:
            money_note = 5
        elif money_note == 5:
            money_note = 2
        elif money_note == 2:
            money_note = 1
        total_money_note = 0
        if withdraw == 0:
            break
print(f'{"-=" * 20}\n Program finalized. Come back soon!')
