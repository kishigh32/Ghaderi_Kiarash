number = int(input("Enter a number please: "))

while number > 0:
    # %10 returns the last digit on the right
    print(number % 10)
    # dividing by 10 shaves off the last digit on the right
    number = int(number / 10)

