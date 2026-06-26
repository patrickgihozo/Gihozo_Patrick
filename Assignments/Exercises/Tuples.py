phones = ("samsung", "iphone", "tecno", "redmi")

# My favorite phone brand
print(phones[0])

#Print the 2nd last item
print(phones[-2])

#Update "iphone" to "itel"
phone_list = list(phones)
phone_list[1] = "itel"
phones = tuple(phone_list)
print(phones)

#Add "Huawei" to the tuple
phones = phones + ("Huawei",)
print(phones)

#Loop through the tuple
for phone in phones:
    print(phone)

#Remove/delete the first item
phone_list = list(phones)
phone_list.pop(0)
phones = tuple(phone_list)
print(phones)

#Create a tuple of Ugandan cities using tuple() constructor
cities = tuple(("Kampala", "Mbarara", "Gulu", "Jinja", "Mbale"))
print(cities)

#Unpack the tuple
city1, city2, city3, city4, city5 = cities
print(city1)
print(city2)

# Print the 2nd, 3rd and 4th cities
print(cities[1:4])

# Join two tuples
first_names = ("Patrick", "Isaac")
second_names = ("Gihozo", "John")

names = first_names + second_names
print(names)

# Create a tuple of colors and multiply by 3
colors = ("red", "blue", "green")
print(colors * 3)

#Count number of times 8 appears
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))