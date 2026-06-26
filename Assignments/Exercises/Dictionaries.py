Shoes = {
    "brand": "Nike",
    "color": "black",
    "size": 40
}

# print the value of shoe size
print(Shoes["size"])

#Change Nike to Adidas
Shoes["brand"] = "Adidas"
print(Shoes)

#Add a new key/value pair
Shoes["type"] = "sneakers"
print(Shoes)

#Return all keys
print(Shoes.keys())

#Return all values
print(Shoes.values())

#check if "size" exists
if "size" in Shoes:
    print("Key exists")
else:
    print("Key does not exist")

#Loop through the dictionary
for key, value in Shoes.items():
    print(key, ":", value)

# Remove "color"
Shoes.pop("color")
print(Shoes)

# Empty the dictionary
Shoes.clear()
print(Shoes)

# copy of a dictionary
student = {
    "name": "Patrick",
    "age": 12,
    "course": "Software Engineering"
}

student_copy = student.copy()
print(student_copy)

# Nested dictionaries
students = {
    "student1": {
        "name": "Patrick",
        "age": 12
    },
    "student2": {
        "name": "Xavier",
        "age": 15
    }
}

print(students)