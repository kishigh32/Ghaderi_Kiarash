word = input("Enter a word please: ")
number = int(input("Enter a number please: "))
word2 = input("Enter a another word please: ")
number2 = int(input("Enter a number please: "))
word3 = input("Enter a word please: ")
number3 = int(input("Enter a number please: "))
word4 = input("Enter a word please: ")
number4 = int(input("Enter a number please: "))
def printTri(word, number):
    for i in range(len(word) - 1, len(word)):
        print(number * word)


printTri(word, number)
printTri(word2, number2)
printTri(word3, number3)
printTri(word4, number4)

