lettersList = []
lettersList.append(["a", "b", "c", "d"])
lettersList.append(["e", "f", "g", "h"])
lettersList.append(["i", "j", "k", "l"])
lettersList.append(["m", "n", "o", "p"])

print("\nHere is a list with letters...")

for letters in lettersList:
    output = ""
    for letter in letters:
        output += letter + "\t"
    print(output)

print("\n\nHere is a list of words using split()\n")
wordsList = []

go = "father mother eagle house car office coffee make create laugh cry photo"
spList = go.split(" ")
print(spList)

spot = 0

print("\n\nPrint the grid...\n")
for i in range(0, 3):
    output = ""
    wordsList.append([])
    for j in range(0, 4):
        wordsList[i].append(spList[spot])
        output += wordsList[i][j]
        spot += 1
    print(output)

