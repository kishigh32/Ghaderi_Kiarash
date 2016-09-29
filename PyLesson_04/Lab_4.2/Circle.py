def format(area):
    output = "{:0.5f}".format(area)
    return output


r = float(input("Enter the radius of a circle:"))
area = 3.14159 * r**2

print("The area of a circle with a radius of" ,r, "is" ,format(area), ".")
