grad1 = input("Please enter your first class letter grade:")
grad2 = input("Please enter your second class letter grade:")
grad3 = input("Please enter your third class letter grade:")
grad4 = input("Please enter your fourth class letter grade:")
grad5 = input("Please enter your fifth class letter grade:")
grad6 = input("Please enter your sixth class letter grade:")
grad7 = input("Please enter your seventh class letter grade:")


def calcPoints(grad):
    if grad == "A":
        return 4.0
    elif grad == "B":
        grad = 3.0
    elif grad == "C":
        grad = 2.0
    elif grad == "D":
        grad = 1.0
    else:
        grad = 0.0
    average = 1234
    print("Your GPA is {:0.2f}".format(average) + ".")

