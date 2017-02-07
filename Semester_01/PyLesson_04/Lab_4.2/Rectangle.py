length = float(input("Enter the length of your rectangle in feet:"))
width = float(input("Enter the width of your rectangle in feet:"))
perimeter = 0

def calcPerim():
    global perimeter
    perimeter = "{:0.5f}".format(2*(length+width))


def display():
    print("Your rectangle is" ,perimeter, "ft around.")


calcPerim()
display()
