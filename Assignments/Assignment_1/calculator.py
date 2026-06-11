print("BILL SPLIT CALCULATOR")

bill_amount = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))

print("\nChoose a tip percentage:")
print("1. 10%")
print("2. 15%")
print("3. 20%")
print("4. Custom")

choice = input("Enter your choice (1-4): ")

# Determine tip percentage
if choice == "1":
    tip_percentage = 10
elif choice == "2":
    tip_percentage = 15
elif choice == "3":
    tip_percentage = 20
elif choice == "4":
    tip_percentage = float(input("Enter custom tip percentage: "))
else:
    print("Invalid choice. Defaulting to 10%.")
    tip_percentage = 10

# Input validation
if bill_amount <= 0:
    print("Error: Bill amount must be greater than 0.")
elif people <= 0:
    print("Error: Number of people must be greater than 0.")
elif tip_percentage < 0:
    print("Error: Tip percentage cannot be negative.")
else:
    tip_amount = bill_amount * tip_percentage / 100
    total_bill = bill_amount + tip_amount
    amount_per_person = total_bill / people

    # Receipt
    print("\nRECEIPT ")
    print(f"Original Bill: {bill_amount:.2f}")
    print(f"Tip Percentage: {tip_percentage}%")
    print(f"Tip Amount: {tip_amount:.2f}")
    print(f"Total Bill: {total_bill:.2f}")
    print(f"Number of People: {people}")
    print(f"Each Person Pays: {amount_per_person:.2f}")