def format(txt, prc):
    print("{:>10} {:*>10.2f}".format(txt, prc))


txt1 = input("Please enter item 1:")
prc1 = float (input("Please enter the price:"))

txt2 = input("Please enter item 2:")
prc2 = float (input("Please enter the price:"))

txt3 = input("Please enter item 3:")
prc3 = float (input("Please enter the price:"))

print("<<<<<<<Receipt>>>>>>>>")
format(txt1, prc1)
format(txt2, prc2)
format(txt3, prc3)








