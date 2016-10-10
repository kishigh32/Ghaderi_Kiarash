def format(item):
    print("*{:>25}{:>25}*".format(item))

item1 = float(input("Please enter the price of the first item:"))
item2 = float(input("Please enter the price of the second item:"))
item3 = float(input("Please enter the price of the third item:"))
item4 = float(input("Please enter the price of the fourth item:"))
subtotal = item1 + item2 + item3 + item4

print("Value of subtotal is" ,subtotal)
if subtotal >= 2000:
    discount = subtotal * 0.15
    tax = (subtotal - subtotal * 0.15) * 0.08
    total = subtotal - discount + tax




if subtotal < 2000:
    discount = 0
    tax = subtotal * 0.08
    total = subtotal + tax




print("<<<<<<<<<<<<<<<<<<<<<<Receipt>>>>>>>>>>>>>>>>>>>")
format(item1)
format(item2)
format(item3)
format(item4)
