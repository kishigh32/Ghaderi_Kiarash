number = int(input("Enter a number please: "))
sum = 0
num = number

while num > 0:
    sum = sum + (num % 10)
    num = int(num/10)

print("The sum of the digits in", number, "is" ,sum)

