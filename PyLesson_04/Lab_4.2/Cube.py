def format(sa):
    output = "{:0.5f}".format(sa)
    return output


side = float(input("Enter the value of your side:"))
sa = 6 * side**2


print("The surface area of a cube with" ,side, "sides is" ,format(sa), ".")
