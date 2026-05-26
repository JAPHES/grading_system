                                 #SEND TO ictlabs@ttu.ac.ke

print("Welcome to Our Taita Taveta Shoping Center")

customer_name = input("Enter customer name: ")
customer_age = int(input("Enter customer age: "))

print(f"Hello {customer_name}, you are {customer_age} years old. Welcome to Our Taita Taveta shoping center!")

item1_name = input("Enter first item name: ")
item1_quantity = int(input("Enter first item quantity: "))
item1_price = float(input("Enter first item price per unit in KES: "))
item1_total = item1_quantity * item1_price


item2_name = input("Enter second item name: ")
item2_quantity = int(input("Enter second item quantity: "))
item2_price = float(input("Enter second item price per unit in KES: "))
item2_total = item2_quantity * item2_price


item3_name = input("Enter third item name: ")
item3_quantity = int(input("Enter third item quantity: "))
item3_price = float(input("Enter third item price per unit in KES: "))
item3_total = item3_quantity * item3_price


subtotal = item1_total + item2_total + item3_total
vat = subtotal * 0.16
grand_total = subtotal + vat


print()
print("========== Taita Taveta Shoping Center ==========")
print(f"Customer Name: {customer_name}")
print(f"Customer Age: {customer_age}")
print("----------------------------------------")
print(f"{item1_name}: {item1_quantity} x KES {item1_price:.2f} = KES {item1_total:.2f}")
print(f"{item2_name}: {item2_quantity} x KES {item2_price:.2f} = KES {item2_total:.2f}")
print(f"{item3_name}: {item3_quantity} x KES {item3_price:.2f} = KES {item3_total:.2f}")
print("----------------------------------------")
print(f"Subtotal: KES {subtotal:.2f}")
print(f"VAT 16%: KES {vat:.2f}")
print(f"Grand Total: KES {grand_total:.2f}")
print("---------------------")


cash_paid = float(input("Enter cash paid in KES: "))

if cash_paid >= grand_total:
    change = cash_paid - grand_total
    print(f"Change due: KES {change:.2f}")
else:
    shortfall = grand_total - cash_paid
    print(f"You have a shortfall of KES {shortfall:.2f}.")
