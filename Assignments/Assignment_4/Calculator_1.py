def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def square(a):
    return a ** 2

def exponent(a, b):
    return a ** b

print("=== SIMPLE CALCULATOR ===")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Exponent")

choice = int(input("Choose an operation (1-7): "))

if choice in [1, 2, 3, 4, 6]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", divide(num1, num2))

elif choice == 5:
    num = float(input("Enter a number: "))
    print("Result:", square(num))

else:
    print("Invalid choice")