name = "Kiarash Ghaderi"
units = 1500000

if units >= 1000000:
    category = "Top Seller"

if units >= 500000:
    category = "Good Seller"

if units >= 100000:
    category = "Average Seller"

if units < 100000:
    category = "Needs Review"

print(name + " = " + category)


print(50 * "_")

name = "Kiarash Ghaderi"
units = 1500000

if units >= 1000000:
    category = "Top Seller"

elif units >= 500000:
    category = "Good Seller"

elif units >= 100000:
    category = "Average Seller"

elif units < 100000:
    category = "Needs Review"

print(name + " = " + category)
