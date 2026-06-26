# Create a set of 3 favorite beverages
beverages = set(("Milk", "Coffee", "Juice"))
print(beverages)

# 2. Add 2 more items
beverages.add("Tea")
beverages.add("Soda")
print(beverages)

# Check if microwave is present
mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("Microwave is present")
else:
    print("Microwave is not present")

# Remove kettle
mySet.remove("kettle")
print(mySet)

# Loop through the set
for item in mySet:
    print(item)

# Add elements from a list to a set
items = {"book", "pen", "bag", "desk"}
new_items = ["phone", "laptop"]

items.update(new_items)
print(items)

# Join two sets
ages = {21, 22, 23}
names = {"Patrick", "John", "Mary"}

combined = ages.union(names)
print(combined)