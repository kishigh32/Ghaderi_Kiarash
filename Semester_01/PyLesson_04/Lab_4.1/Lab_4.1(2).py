def format(volume):
    output = "{:.4f}".format(volume)
    return output

height = float(input("Enter the height in inches:"))
length = float(input("Enter the length in inches:"))
width = float(input("Enter the width in inches:"))
volume = height * length * width / 1728
print("The volume of your subwoofer box is" ,format(volume), "in feet.")
