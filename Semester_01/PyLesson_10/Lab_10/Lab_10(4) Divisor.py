numsList = []
import random


for i in range(0, 4):
    numsList.append([])
    for j in range(0,4):
        numsList[i].append(random.randint(1,1001))


for nums in numsList:
    output = ""
    for num in nums:
        output += str(num) + " "
    print(output)

div = int(input("Enter a number please: "))
count = 0

for nums in numsList:
    for num in nums:
        if num % div == 0:
            count += 1

print("There are", count, "numbers divisible by", div, "in the List.")

