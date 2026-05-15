
def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(f"{city}, {state} {zip_code}")


name = "Naomi Tewolde"
address = "123 Main St"
city = "Charlotte"
state = "NC"
zip_code = "28202"

display_mailing_label(name, address, city, state, zip_code)

#OUTPUT:
#Naomi Tewolde
#123 Main St
#Charlotte, NC 28202


#def/return using add_numbers()

def add_numbers(*numbers):
    total = sum(numbers)
    
    # Create formatted equation string
    equation = " + ".join(str(num) for num in numbers)
    
    print(f"{equation} = {total}")

add_numbers(7, 13, 21)
add_numbers(4, 9, 15, 20)
add_numbers(100, 250)

#OUTPUT
#7 + 13 + 21 = 41
#4 + 9 + 15 + 20 = 48
#100 + 250 = 350


# Function 3: display receipt
def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due}")
    print(f"Amount Paid: ${amount_paid}")
    
    if amount_paid > total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change}")
    elif amount_paid == total_due:
        print("Change Due: $0")
    else:
        remaining = total_due - amount_paid
        print(f"Remaining Balance: ${remaining}")


#c) Call display_receipt() three times
print("Receipts:\n")

# Overpay
display_receipt(50, 70)
print()

# Exact pay
display_receipt(30, 30)
print()

# Underpay
display_receipt(45, 20)

#OUTPUT 

#Receipts:

#Total Due: $50
#Amount Paid: $70
#Change Due: $20

#Total Due: $30
#Amount Paid: $30
#Change Due: $0

#Total Due: $45
#Amount Paid: $20
#Remaining Balance: $25