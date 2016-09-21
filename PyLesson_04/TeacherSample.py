def format (item, price):
    print("{:<10}""{:<10.2f}".format(item, price))


#input item1
item1 = input("please enter item:")
price1 = float(input("please enter the price:"))

#input item2
item2 = input("please enter item:")
price2 = float(input("please enter the price:"))
               
#input item3
item3 = input("please enter item:")
price3 = float(input("please enter the price:"))

#calculate subtotal
#subtotal = #add all prices together

print("<<<<<<<<<<<receipt>>>>>>>>>>>>")
format(item1, price1)
format(item2, price2)
#format("subtotal:" ,subtotal)
#same thing for tax, and total
print("_______________________________________")
#print "thank you" message here
