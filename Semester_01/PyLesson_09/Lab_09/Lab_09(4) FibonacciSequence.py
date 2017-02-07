num = int(input("Enter your starting number please: "))
size = int(input("Enter your sequence size please: "))

seq = []


for i in range(0, size):
    if i == 1 or i == 0:
        seq.append(num)
    else:
        seq.append(seq[i-1] + seq[i-2])
    print(seq[i], " ")

