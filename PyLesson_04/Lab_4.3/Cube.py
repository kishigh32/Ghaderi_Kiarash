def setNums():
    global side
    side = float(input("Enter the value of your side:"))

def calcSurf():
    output = "{:0.5f}".format(6 * side**2)
    return output

setNums()
print("The surface area of a cube whose sides are" ,side, "in length is" ,calcSurf(), ".")
