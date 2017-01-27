import random
class Item:
    def __init__(self, iManufacturer, iName, iCategory = "", iPrice = ""):
        self.itemManufacturer = iManufacturer
        self.itemName = iName
        self.itemCategory = iCategory
        self.itemPrice = iPrice
        self.userUPC = random.randint(1000000000, 10000000000)

    def setIDK(self, newItemManufacturer, newItemName, newItemCategory, newItemPrice):
        self.itemManufacturer = newItemManufacturer
        self.itemName = newItemName
        self.itemCategory = newItemCategory
        self.itemPrice = newItemPrice
        self.userUPC = random.randint(1000000000, 10000000000)

    def getItemManufacturer(self):
        return self.itemManufacturer

    def getItemName(self):
        return self.itemName

    def getItemCategory(self):
        return self.itemCategory

    def getItemPrice(self):
        return self.itemPrice

    def getUserUPC(self):
        return self.userUPC

    def __str__(self):
        print("Custom info...\nItem Manufacturer: ", self.itemManufacturer, "\nItem Name: ", self.itemName, "\nItem Category: ", self.itemCategory, "\nItem Price: ", self.itemPrice, "\nUser UPC: ", self.userUPC)

def main():
    iManufacturer = input("Enter your item manufacturer please: ")
    iName = input("Enter your item name please: ")
    ctg = input("Would you like to use a item category?(y or n): ")
    if ctg == "n":
        item1 = Item(iManufacturer, iName)
    else:
        iCategory = input("Enter your item category please: ")
        iPrice = int(input("Enter your item price please: "))
        item1 = Item(iManufacturer, iName, iCategory, iPrice)

    print(item1.__str__())

main()

