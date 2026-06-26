
names = ["Patrick", "John", "Mary", "Alice", "David"]
print(names[1])

#Change the value of the first item
names[0] = "Peter"
print(names)

#Add sixth item
names.append("Grace")
print(names)

#Add "Bathel" as the 3rd item
names.insert(2, "Bathel")
print(names)

#Remove the 4th item
names.pop(3)
print(names)

#Use negative indexing to print the last item
print(names[-1])

#new list with 7 items and print 3rd, 4th and 5th items
items = ["A", "B", "C", "D", "E", "F", "G"]
print(items[2:5])

#a list of countries and make a copy of it
countries = ["Uganda", "Rwanda", "Kenya", "Tanzania"]
countries_copy = countries.copy()
print(countries_copy)

#Loop through the list of countries
for country in countries:
    print(country)

#Sort animal names in ascending and descending order
animals = ["dog", "cat", "lion", "zebra", "ant"]

animals.sort()
print("Ascending:", animals)

animals.sort(reverse=True)
print("Descending:", animals)

for animal in animals:
    if "a" in animal:
        print(animal)

#Join first names and second names
first_names = ["Patrick", "John"]
second_names = ["Gihozo", "Smith"]

full_names = first_names + second_names
print(full_names)