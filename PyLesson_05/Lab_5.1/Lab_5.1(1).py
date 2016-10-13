def format(average):
    print("{:.2f}".format(average))

grad1 = input("Please enter your first class letter grade:")
grad2 = input("Please enter your second class letter grade:")
grad3 = input("Please enter your third class letter grade:")
grad4 = input("Please enter your fourth class letter grade:")
grad5 = input("Please enter your fifth class letter grade:")
grad6 = input("Please enter your sixth class letter grade:")
grad7 = input("Please enter your seventh class letter grade:")

if grad1 == "A": GPA1 = 4.0
elif grad1 == "B": GPA1 = 3.0
elif grad1 == "C": GPA1 = 2.0
elif grad1 == "D": GPA1 = 1.0
elif grad1 == "F": GPA1 = 0.0
if grad2 == "A": GPA2 = 4.0
elif grad2 == "B": GPA2 = 3.0
elif grad2 == "C": GPA2 = 2.0
elif grad2 == "D": GPA2 = 1.0
elif grad2 == "F": GPA2 = 0.0
if grad3 == "A": GPA3 = 4.0
elif grad3 == "B": GPA3 = 3.0
elif grad3 == "C": GPA3 = 2.0
elif grad3 == "D": GPA3 = 1.0
elif grad3 == "F": GPA3 = 0.0
if grad4 == "A": GPA4 = 4.0
elif grad3 == "B": GPA4 = 3.0
elif grad4 == "C": GPA4 = 2.0
elif grad4 == "D": GPA4 = 1.0
elif grad4 == "F": GPA4 = 0.0
if grad5 == "A": GPA5 = 4.0
elif grad4 == "B": GPA5 = 3.0
elif grad5 == "C": GPA5 = 2.0
elif grad5 == "D": GPA5 = 1.0
elif grad5 == "F": GPA5 = 0.0
if grad6 == "A": GPA6 = 4.0
elif grad5 == "B": GPA6 = 3.0
elif grad6 == "C": GPA6 = 2.0
elif grad6 == "D": GPA6 = 1.0
elif grad6 == "F": GPA6 = 0.0
if grad7 == "A": GPA7 = 4.0
elif grad7 == "B": GPA7 = 3.0
elif grad7 == "C": GPA7 = 2.0
elif grad7 == "D": GPA7 = 1.0
elif grad7 == "F": GPA7 = 0.0

average = (GPA1 + GPA2 + GPA3 + GPA4 + GPA5 + GPA6 + GPA7)/7
format("Your GPA is" ,average)
