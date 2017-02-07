one = int(input("Enter the first number:"))
two = int(input("Enter the second number:"))

even = (one + two) % 2 == 0

if even:
    print(one + two, "is even!")

if not even:
    print(one + two, "is odd!")

