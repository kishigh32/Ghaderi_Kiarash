num1 = 3
num2 = 4
sum = 0


def mkSum():
    global sum, num1, num2
    sum = num1 + num2

def numPrint():
    global sum, num1, num2
    print(num1, "plus" , num2, "equals" ,sum)

mkSum()
numPrint()
