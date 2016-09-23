
def format(txt, prc):
    print("*{:>10} {:.>10.2f}\n".format(txt, prc))


txt1 = input("Please enter item 1:")
prc1 = float (input("Please enter the price:"))

txt2 = input("Please enter item 2:")
prc2 = float (input("Please enter the price:"))

txt3 = input("Please enter item 3:")
prc3 = float (input("Please enter the price:"))

subtotal = prc1 + prc2 + prc3
tax = subtotal * 0.08
total = subtotal + tax

print("<<<<<<<___Receipt___>>>>>>>")
format(txt1, prc1)
format(txt2, prc2)
format(txt3, prc3)
format("  Subtotal:" ,subtotal)
format("       Tax:" ,tax)
format("     Total:" ,total)
print("_____________________________\n  Thank you for your support")




