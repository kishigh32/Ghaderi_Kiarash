num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))
num3 = float(input("Enter your third number:"))
avg = 0

def average():
    global avg
    avg = "{:0.5f}".format((num1 + num2 + num3)/3)

def display():
    print("The average of",num1,",",num2,"and",num3,"is",avg,".")

average()
display()
