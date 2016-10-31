side = float(input("Enter the value of your side:"))
sa = 0

def calcSurf():
    global sa
    sa = "{:0.5f}".format(6 * side**2)

def display():
    print("The surface area of a cube whose sides are" ,side, "in length is" ,sa, ".")


calcSurf()
display()
