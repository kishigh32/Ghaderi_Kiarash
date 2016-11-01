number = int(input("Enter a number please: "))
output = ""

for numbs in range(1, number + 1):
    output = output + str(numbs) + " * "
print(number, "! = ", output)

