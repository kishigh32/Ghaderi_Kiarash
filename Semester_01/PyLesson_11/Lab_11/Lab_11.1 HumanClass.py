class human:
    def __init__(self, h, e, s):
        self.hair = h
        self.eyes = e
        self.skin = s

    def setHES(self, newHair, newEyes, newSkin):
        self.hair = newHair
        self.eyes = newEyes
        self.skin = newSkin

    def getHair(self):
        return self.hair

    def getEyes(self):
        return self.eyes

    def getSkin(self):
        return self.skin

def main():
    hair = input("Enter your hair color: ")
    eyes = input("Enter your eyes color: ")
    skin = input("Enter your skin color: ")

    personalities = human(hair, eyes, skin)

    print("My info...")
    print("Hair: black")
    print("Eyes: brown")
    print("Skin: eastern white\n\n")

    print("Your info...")
    print("Hair:", personalities.getHair())
    print("Eyes:", personalities.getEyes())
    print("Skin:", personalities.getSkin())

main()

