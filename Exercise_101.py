from datetime import date


def votation(year_of_birth):
        if date.today().year - year_of_birth < 18:
            return (f"With {date.today().year - year_of_birth} years you can't vote.")
        elif 18 <= (date.today().year - year_of_birth) < 64:
            return (f"With {date.today().year - year_of_birth} years the voting is mandatory. ")
        else:
            return (f"With {date.today().year - year_of_birth} years the vote is optional.")


print(votation(int(input('Type the year that you was birth: '))))

