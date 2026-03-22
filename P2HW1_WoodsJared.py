# Jared Woods
# 03/08/2026
# P2HW1 - Travel Expenses
# This program calculates and displays travel expenses and remaining budget.

# Get user inputs
budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
hotel = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

# Calculate remaining balance
expenses = gas + hotel + food
remaining = budget - expenses

print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${hotel:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")
print("---------------------------------------")
print(f"\nRemaining Balance: ${remaining:,.2f}")
