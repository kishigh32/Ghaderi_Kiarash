def format(ret):
    output = "{:.3f}".format(ret)
    return output

r = float(input("Enter the the interest rate:"))
P = float(input("Enter the initial money you recieved from bank:"))
n = float(input("Enter the number of times the loan is compounded per year:"))
t = float(input("Enter the life of the loan in years:"))
total = P * (1 + r / n)**(n * t)
ret = total * 12 / t
print("Your total payment is" ,total)
print("However, your return amount is" ,format(ret))
