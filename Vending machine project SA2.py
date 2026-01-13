# Dictionary storing item code, name, and price
items = {
    "A1": ("Water", 1.00),
    "A2": ("Cola", 1.50),
    "B1": ("Chips", 1.20),
    "B2": ("Chocolate", 1.30)
}

# Main loop allows multiple purchases
while True:
    # Display vending machine menu
    print("\nVENDING MACHINE")
    for code, item in items.items():
        print(f"{code} - {item[0]} (£{item[1]})")

    # Get user item selection
    choice = input("Enter item code: ").upper()

    # Check if entered code exists
    if choice not in items:
        print("Invalid selection")
        continue

    # Get selected item price
    price = items[choice][1]

    # Ask user to insert money
    try:
        money = float(input("Insert money: £"))
    except:
        print("Invalid amount")
        continue

    # Check if enough money was inserted
    if money < price:
        print("Not enough money")
        continue

    # Calculate and round the change
    change = round(money - price, 2)

    # Dispense item and return change
    print(f"{items[choice][0]} dispensed")
    print(f"Change returned: £{change}")

    # Ask if the user wants to continue
    again = input("Buy another item? (y/n): ").lower()
    if again != "y":
        print("Thank you")
        break
