print("  E-COMMERCE SYSTEM   ")

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin":

    if password == "admin123":
        role = "Admin"
        print("\nLogin Successful!")
        print("Welcome Admin")
        print("Access Level: All Features")

    else:
        print("Wrong Password!")
        print("Access Denied!")
        exit()

elif username == "cashier":

    if password == "cash123":
        role = "Cashier"
        print("\nLogin Successful!")
        print("Welcome Cashier")
        print("Access Level: Billing and Sales")

    else:
        print("Wrong Password!")
        print("Access Denied!")
        exit()

elif username == "customer":

    if password == "cust123":
        role = "Customer"
        print("\nLogin Successful!")
        print("Welcome Customer")
        print("Access Level: View Purchases")

    else:
        print("Wrong Password!")
        print("Access Denied!")
        exit()

else:
    print("Invalid Username!")
    print("Access Denied!")
    exit()

print("\n PRODUCT PURCHASE ")

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
        print("Invalid Coupon Code!")

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
        print("Invalid Coupon Code!")

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
        print("Invalid Coupon Code!")

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

# RECEIPT
print("\n RECEIPT ")
print("User Role:", role)
print("Subtotal:", subtotal)
print("Discount Rate:", discount_rate, "%")
print("Discount Amount:", discount_amount)
print("Coupon Discount:", coupon_discount)
print("Tax Rate:", tax_rate, "%")
print("Tax Amount:", tax_amount)
print("Final Price:", final_price)
