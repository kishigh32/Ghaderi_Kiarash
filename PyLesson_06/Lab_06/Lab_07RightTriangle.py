word = input("Enter a word please: ")

def printTri():
    for i in range(len(word), -1, -1):
        print(word[i:len(word)])

printTri()
