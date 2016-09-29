def format(average):
    output = "{:0.5f}".format(average)
    return output


num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))
num3 = float(input("Enter your third number:"))
average = (num1 + num2 + num3) / 3


print("The average of",num1,",",num2,"and",num3,"is",format(average),".")

