r = float(input("Enter the radius of a circle:"))

def calcArea():
    output = "{:0.5f}".format(3.14159 * r**2)
    return output


def display():
    print("The area of a circle with a radius of" ,r, "is" ,calcArea(), ".")


calcArea()
display()
