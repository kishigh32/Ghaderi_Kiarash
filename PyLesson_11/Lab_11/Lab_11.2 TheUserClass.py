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
        return self.userID
    
    def __str__(self):
        print("Custom info...\nFirst Name: ", self.firstName, "\nLast Name: ", self.lastName, "\nAvatar: ", self.avatar, "\nUser ID#: ", self.userID)

    
def main():
    fName = input("Enter your first name please: ")
    lName = input("Enter yout last name please: ")
    avt = input("Would you like to use a public avatar?(y or n): ")
    if avt == "n":
        user1 = User(fName, lName)
    else:
        avat = input("Enter your avatar please: ")
        user1 = User(fName, lName, avat)

    print(user1.__str__())

main()




