# Vendor Details and Annual Purchase Report

vendor_name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

total_purchase = 0

print("\nEnter monthly purchase amounts:")

for month in range(1, 13):
    amount = float(input(f"Month {month}: "))
    total_purchase += amount

print("\n--- Vendor Details ---")
print("Vendor Name:", vendor_name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Annual Purchase Amount:", total_purchase)