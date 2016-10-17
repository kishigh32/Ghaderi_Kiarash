grad1 = input("Please enter your first class letter grade:")
grad2 = input("Please enter your second class letter grade:")
grad3 = input("Please enter your third class letter grade:")
grad4 = input("Please enter your fourth class letter grade:")
grad5 = input("Please enter your fifth class letter grade:")
grad6 = input("Please enter your sixth class letter grade:")
grad7 = input("Please enter your seventh class letter grade:")


def calcPoints(gpa):
    if grad == "A":
        gpa = 4.0
    elif grad == "B":
        gpa = 3.0
    elif grad == "C":
        gpa = 2
    elif grad == "D":
        gpa = 1.0
    else:
        gpa = 0.0
    average = (calcPoints(gpa1) + calcPoints(gpa2) + calcPoints(gpa3) + calcPoints(gpa4) + calcPoints(gpa5) + calcPoints(gpa6) + calcPoints(gpa7))/7
    print("Your GPA is {:0.2f}".format(average) + ".")

