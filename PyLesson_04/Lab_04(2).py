def format(ins, out):
    print("{:>25}{:>25}".format(ins, out))

ins1 = input("Enter your first name:")
out1 = input("Enter your last name:")
ins3 = input("Enter your job:")
ins2 = input("Enter the school name:")
out2 = input("Enter the school year:")
out3 = input("Enter your subject:")

print("*" * 50)
format(ins2, out2)
format(ins1, out1)
format(ins3, out3)
print("*" * 50)
