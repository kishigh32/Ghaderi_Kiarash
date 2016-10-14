def format(average):
    output = "{:.2f}".format(average)
    return output


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
        return 3.0
    elif grad == "C":
        return 2
    elif grad == "D":
        return 1.0
    else:
        return 0.0

average = (calcPoints(grad1), + calcPoints(grad2), + calcPoints(grad3), + calcPoints(grad4), + calcPoints(grad5), + clacPoints(grad6), + calcPoints(grad7),) / 7

print("Your GPA is" ,format(average), ".")
