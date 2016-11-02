word = input("Enter a word please: ")

def printTri():
    for i in range(0, len(word), -1):
        print(word[0:i])

printTri()
