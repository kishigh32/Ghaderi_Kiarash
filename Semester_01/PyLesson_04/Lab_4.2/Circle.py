r = float(input("Enter the radius of a circle:"))
area = 0

def calcArea():
    global area
    area = "{:0.5f}".format(3.14159 * r**2)


def display():
    print("The area of a circle with a radius of" ,r, "is" ,area, ".")


calcArea()
display()

