grade = int(input("Enter a grade: "))
if (grade > 120 or grade < 0):
    print("Bad grade")
else:
    if (grade >= 95):
        final = "A"
    elif (grade >= 75):
        final = "B"
    elif (grade >= 50):
        final = "C"
    else:
        final = "F"
    print(final)

