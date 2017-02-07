word = input("Enter a word please: ")
number = int(input("Enter a number please: "))

def printTri():
    for i in range(len(word) - 1, len(word)):
        print(number * word)

printTri()
