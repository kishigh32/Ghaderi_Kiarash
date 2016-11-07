word = "Na"
word1 = "Hey"
word2 = "Goodbye!"

def printTri():
    global word, word1, word2
    for i in range(len(word), len(word) + 1):
        print(len(word) * word[0:i])

printTri()
