def setNums():
    global num1, num2, num3
    num1 = float(input("Enter your first number:"))
    num2 = float(input("Enter your second number:"))
    num3 = float(input("Enter your third number:"))

def average():
    output = "{:0.5f}".format((num1 + num2 + num3)/3)
    return output

setNums()
print("The average of",num1,",",num2,"and",num3,"is",average(),".")
