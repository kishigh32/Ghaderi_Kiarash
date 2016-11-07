number = int(input("Enter a number please: "))
table = int(input("Enter a number for table size please: "))

def printTri():
    global number, table
    for i in range(1, table):
        print(i, " | ", number * i)

printTri()
