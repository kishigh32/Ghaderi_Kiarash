equation = input("Enter a mathematical expression please: ")



while i < len(equation):
    if i < len(equation) and (equation.append("*" or "/")):
        if equation.append("*"):
            equation.append(int(i-1) * int(i+1))
        else:
            equation.append(int(i-1) / int(i+1))
        equation.remove(i-1)
        equation.remove(i)
    i += 1

i = 0

while i < len(equation):
    if i < len(equation) and (equation.append("+" or "-")):
        if equation.append("+"):
            equation.append(int(i-1) + int(i+1))
        else:
            equation.append(int(i-1) - int(i+1))
        equation.remove(i-1)
        equation.remove(i)
    i += 1

print(equation)

