words = ["I", "am", "Kiarash", "Ghaderi", "KG"]

print("In order...")

output = ""
for i in words:
    output += i + " "

print(output)
print()
print("Reversed...")


def reverse(words):
    newput = ""
    for k in range(len(words),0,-1):
        newput += words[k-1] + " "
    print(newput)

reverse(words)

