print("===== E-COMMERCE SYSTEM =====")


users = {
    "Admin": "admin123",
    "Cashier": "cash123",
    "Customer": "cust123"
}

access_levels = {
    "Admin": "All Features",
    "Cashier": "Billing and Sales",
    "Customer": "View Purchases"
}

max_attempts = 3
attempts = 0

while attempts < max_attempts:

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users:

        if users[username] == password:

            role = username

            print("\nLogin Successful!")
            print("Welcome", role)
            print("Access Level:", access_levels[role])

            break

        else:
            print("Incorrect Password!")

    else:
        print("Username Not Found!")

    attempts += 1
    print("Attempts Remaining:", max_attempts - attempts)

if attempts == max_attempts:
    print("\nMaximum login attempts reached.")
    print("Access Denied!")
    exit()

print("\n===== PRODUCT PURCHASE =====")

subtotal = float(input("Enter Product Subtotal: "))
coupon = input("Enter Coupon Code: ")
location = input("Enter Location (Uganda, Rwanda, Kenya): ")


if subtotal >= 500000:

    discount_rate = 20

    if coupon == "VIP":
        coupon_rate = 30

    elif coupon == "SAVE20":
        coupon_rate = 20

    elif coupon == "SAVE10":
        coupon_rate = 10

    else:
        coupon_rate = 0

elif subtotal >= 200000:

    discount_rate = 10

    if coupon == "VIP":
        coupon_rate = 20

    elif coupon == "SAVE20":
        coupon_rate = 15

    elif coupon == "SAVE10":
        coupon_rate = 5

    else:
        coupon_rate = 0

elif subtotal >= 100000:

    discount_rate = 5

    if coupon == "VIP":
        coupon_rate = 10

    elif coupon == "SAVE20":
        coupon_rate = 5

    elif coupon == "SAVE10":
        coupon_rate = 3

    else:
        coupon_rate = 0

else:

    discount_rate = 0

    if coupon == "VIP":
        coupon_rate = 5
    else:
        coupon_rate = 0


match location:

    case "Uganda":
        tax_rate = 18

    case "Rwanda":
        tax_rate = 15

    case "Kenya":
        tax_rate = 16

    case _:
        tax_rate = 20

discount_amount = subtotal * discount_rate / 100

coupon_discount = subtotal * coupon_rate / 100

amount_after_discount = subtotal - discount_amount - coupon_discount

tax_amount = amount_after_discount * tax_rate / 100

final_price = amount_after_discount + tax_amount

print("\n      RECEIPT     ")
print("User Role:", role)
print("Subtotal:", subtotal)

print("Normal Discount Rate:", discount_rate, "%")
print("Normal Discount Amount:", discount_amount)

print("Coupon Discount Rate:", coupon_rate, "%")
print("Coupon Discount Amount:", coupon_discount)

print("Tax Rate:", tax_rate, "%")
print("Tax Amount:", tax_amount)

print("---------------------------")
print("Final Price:", final_price)
print("===========================")