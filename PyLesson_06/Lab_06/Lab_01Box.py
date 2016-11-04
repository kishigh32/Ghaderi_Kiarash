word = input("Enter a word please: ")

def printTri():
    for i in range(len(word), len(word) + 1):
        print((len(word)) * word[0:i])

printTri()

wor = input("Enter a word please: ")

def printTri():
    for i in range(0, len(word) + 1):
        al = chr(wor)
        print(al, end=" ")
        wor = wor + 1
        


printTri()


