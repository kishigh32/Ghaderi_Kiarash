side = 999
sa = 0

def setNums():
    global side
    side = float(input("Enter the value of your side:"))

def calcSurf():
    global sa
    sa = "{:0.5f}".format(6 * side**2)

setNums()
calcSurf()
print("The surface area of a cube whose sides are" ,side, "in length is" ,sa, ".")
