num1 = 3
num2 = 2
num1 = 1
avg = 0

def setNums():
    global num1, num2, num3
    num1 = float(input("Enter your first number:"))
    num2 = float(input("Enter your second number:"))
    num3 = float(input("Enter your third number:"))

def average():
    global avg
    avg = "{:0.5f}".format((num1 + num2 + num3)/3)

setNums()
average()
print("The average of",num1,",",num2,"and",num3,"is",avg,".")
