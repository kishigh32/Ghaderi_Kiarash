user = "ilovecomputer"
pas = "ilovecomputer"


def passCheck():
    user = input("Enter your username: ")
    pas = input("Enter your password: ")
    if user == "ilovecomputer" and pas == "ilovecomputer":
            print("You are granted access! Now you can access nuclear weapons!")
    else:
        if user == "ilovecomputer":
            print("Your password is incorrect!")
            print("Try again")
            passCheck()
        elif pas == "ilovecomputer":
            print("Your username is incorrect!")
            print("Try again")
            passCheck()
        else:
            print("Your username and password are incorrect")
            print("Try again")
            passCheck()


passCheck()
