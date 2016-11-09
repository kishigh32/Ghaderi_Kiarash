def format(item, price):
    print("*{:>15}{:>10.2f}".format(item, price))

item1 = input("Please enter the first item:")
price1 = float(input("Please enter the price of the first item:"))
item2 = input("Please enter the second item:")
price2 = float(input("Please enter the price of the second item:"))
item3 = input("Please enter the third item:")
price3 = float(input("Please enter the price of the third item:"))
item4 = input("Please enter the fourth item:")
price4 = float(input("Please enter the price of the fourth item:"))
subtotal = price1 + price2 + price3 + price4

def Discount():

    if subtotal >= 2000:
        discount = subtotal * 0.15
        tax = (subtotal - discount) * 0.08
        total = subtotal - discount + tax
            
    if subtotal < 2000:
        discount = 0.0
        tax = subtotal * 0.08
        total = subtotal + tax


    print("<<<<<<<<<<Receipt>>>>>>>>>>")
    format(item1, price1)
    format(item2, price2)
    format(item3, price3)
    format(item4, price4)
    format("Subtotal:" ,subtotal)
    format("Discount:" ,discount)
    format("Tax:" ,tax)
    format("Total:" ,total)
    print(27 * "_")
    print("         Thank you")

Discount()


