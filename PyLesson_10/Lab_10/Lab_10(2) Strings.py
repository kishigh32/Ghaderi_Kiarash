go = input("Enter 16 strings please: ")

spList = go.split(" ")
print(spList, "\n")

wordsList = []

spot = 0

for i in range(0, 4):
    output = ""
    wordsList.append([])
    for j in range(0, 4):
        wordsList[i].append(spList[spot])
        output += " " + wordsList[i][j]
        spot += 1
    print(output)
