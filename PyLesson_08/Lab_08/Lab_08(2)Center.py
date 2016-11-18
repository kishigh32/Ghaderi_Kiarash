word1 = input("Enter a word please: ")
word2 = input("Enter a word please: ")
word3 = input("Enter a word please: ")

def makeCenter(word):
    if (len(word) >= 20):
        return word
    else:
        return makeCenter(" " + word + " ")

print(makeCenter(word1))
print(makeCenter(word2))
print(makeCenter(word3))

