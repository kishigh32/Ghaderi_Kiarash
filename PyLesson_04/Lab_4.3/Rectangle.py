def setNums():
    global length, width
    length = float(input("Enter the length of your rectangle in feet:"))
    width = float(input("Enter the width of your rectangle in feet:"))

def calcPerim():
    output = "{:0.5f}".format(2*(length+width))
    return output

setNums()
print("Your rectangle is" ,calcPerim(), "ft around.")
