def getReverse():

    number = int(input("Enter a number please: "))
    num = number
    rev = 0

    while num > 0:
        rev = (rev * 10)
        rev = rev + (num % 10)
        num = int(num / 10)
    print(number, "reversed is", rev)

getReverse()

