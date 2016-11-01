num1 = int(input("Enter your maximum number please: "))
num2 = int(input("Enter the distance between each number please: "))

def printTri():
    for i in range(2, len(num1) + num2, num2):
        print(num1[0:i])

printTri()
