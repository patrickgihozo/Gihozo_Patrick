student = {
    "name": "Patrick",
    "age": 21,
    "course": "Software Engineering",
    "year": 2
}

# 1. Iterate through keys
print("Keys:")
for key in student:
    print(key)

# 2. Iterate through values
print("\nValues:")
for value in student.values():
    print(value)

# 3. Iterate through key-value pairs
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# 4. Access values using keys
print("\nUsing keys to access values:")
for key in student:
    print(f"{key}: {student[key]}")

# 5. Enumerate dictionary items
print("\nNumbered items:")
for index, (key, value) in enumerate(student.items(), start=1):
    print(f"{index}. {key}: {value}")