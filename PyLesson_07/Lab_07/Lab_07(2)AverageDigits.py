number = int(input("Enter a number please: "))
digits = 0
average = 0

num = number

while num > 0:
    digits += 1
    average = average + (num % 10)
    num = int(num / 10)

print("The average of the digits in", number, "is", average/digits)

