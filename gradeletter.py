'''Test if-elif-...-else determining a letter grade.'''


def letterGrade(score):
    """Determines the letter grade from the inputed number"""
    if score < 60 and score >= 0:
        letter = "F"
    elif score < 70 and score >= 60:
        letter = "D"
    elif score < 80 and score >= 70:
        letter = "C"
    elif score < 90 and score >= 80:
        letter = "B"
    elif score >= 90:
        letter = "A"
    return letter


def main():
    # user input only accepts floats
    try:
        x = float(input('Enter a numerical grade: '))
        letter = letterGrade(x)
        print('Your grade is ' + letter + '.')
    except ValueError:
        print("Invalid choice, try again.")
    finally:
        quit


main()