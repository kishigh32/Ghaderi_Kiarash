r = 99
area = 0

def setNums():
    global r
    r = float(input("Enter the radius of a circle:"))

def calcArea():
    global area
    area = "{:0.5f}".format(3.14159 * r**2)


setNums()
calcArea()

print("The area of a circle with a radius of" ,r, "is" ,area, ".")

