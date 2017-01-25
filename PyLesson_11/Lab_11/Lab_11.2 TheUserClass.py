import random
class User:
    def __init__(self, fName, lName, avat = ""):
        self.firstName = fName
        self.lastName = lName
        self.avatar = avat
        self.userID = random.randint(0, 1000000)
        
    def setHES(self, newFirstName, newLastName, newAvatar):
        self.firstName = newFirstName
        self.lastName = newLastName
        self.avatar = newAvatar
        self.userID = random.randint(0, 1000000)

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getAvatar(self):
        return self.avatar

    def getUserID(self):
        return selfuserID
    
    def __str__(self):
        return "Custom info...\nFirst Name: " + self.firstName() + "\nLast Name: " + self.lastName() + "\nAvatar: " + self.avatar() + "User ID#: " + str(self.userID())

    
def main():
    first = input("Enter your first name please: ")
    last = input("Enter yout last name please: ")
    avatar = input("Enter your avatar please: ")
    avt = input("Would you like to use a public avatar?(y or n) ")
    if avt == "n":
        return user1 == User(firstName, lastName)
    else:
        return user1 == User(first, last, avatar)

    print(user1.__str__())

main()




