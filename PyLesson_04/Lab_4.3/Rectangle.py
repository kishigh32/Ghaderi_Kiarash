length = 99
width = 22
avg = 0

def setNums():
    global length, width
    length = float(input("Enter the length of your rectangle in feet:"))
    width = float(input("Enter the width of your rectangle in feet:"))

def calcPerim():
    global avg
    avg = "{:0.5f}".format(2*(length+width))
    

setNums()
calcPerim()

print("Your rectangle is" ,avg, "ft around.")
