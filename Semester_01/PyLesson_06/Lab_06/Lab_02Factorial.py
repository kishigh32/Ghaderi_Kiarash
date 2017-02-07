number = int(input("Enter a number please: "))
output = ""

for numbs in range(1, number):
    output = output + str(numbs) + " * "

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(number, "! = ", output, number, "=", factorial(number))

