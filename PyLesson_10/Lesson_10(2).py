values = []
values.append([1, 2, 3, 4])
values.append([5, 6, 7, 8])
values.append([9, 10, 11, 12])
values.append([13, 14, 15, 16])


print("\nSearch the list...")
count = 0
for value in values:
    for number in value:
        if number % 5 == 0:
            count += 1
print("There are", count, "multiples of 5 in the list")



print("\n\nSearch the list...")
count = ""
for value in values:
    for number in value:
        if number % 5 == 0:
            count += str(number) + ", "
print("The numbers", count, "in the list are multiples of 5")



print("\n\nSearch the list...")
count = 0
for value in values:
    for number in value:
        count += number
print("The sum of the values in the list is equal to", count)
