
def recursion():
    dis = input("Do you think I ever been discriminated?")
    if dis == "yes" or dis == "Yes":
        print("That's right. I have been discriminated my whole life!")
    else:
        print("Well... I have")
    print("I have been hated... many times")
    num = int(input("Guess how many times people made fun of me?"))
    if num >= 1 and num <= 180:
        if num >= 1 and num <= 47:
            print("That was only the first week")
            first = int(input("Now tell me number of bollies on my first day  "))
            if first >= 1 and first <= 16:
                print("I got bollies 16 times on my first day")
            else:
                print("Not in the range")
                recursion()
        else:
            if num > 47 and num <= 120:
                print("Well... I can tell that the number you guessed was passed my first week")
            else:
                print("I can only say it already passed my first month")
    else:
        if num > 180 and num <= 1756:
            print("My lifetime discrimination goes belong your number")
            if num > 180 and num <= 758:
                print("But you guessed it in my first year")
            else:
                print("Well... I don't remember very well, but I think it was for my second year")
        else:
            

recursion()

    
