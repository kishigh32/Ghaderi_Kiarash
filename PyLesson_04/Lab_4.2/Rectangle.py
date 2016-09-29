


def format(perimeter):
    output = "{:0.5f}".format(perimeter)
    return output


length = float(input("Enter the length of the rectangle in feet:"))
width = float(input("Enter the width of the rectangle in feet:"))
perimeter = 2 * (length + width)


print("Your rectangle is" ,format(perimeter), "sq ft around.")
    
    

