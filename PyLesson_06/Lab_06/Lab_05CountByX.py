num1 = int(input("Enter your maximum number please: "))
num2 = int(input("Enter the distance between each number please: "))
output = ""

for i in range(num2, num1 + 1, num2):
    output = output + str(i) + "    "
print(output)

