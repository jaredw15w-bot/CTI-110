# Jared Woods
# 1MAR2026
# P1HW1


"""
PSEUDOCODE:

1. Display program title message
2. Prompt user to enter budget
3. Prompt user to enter travel destination
4. Prompt user to enter amount for gas
5. Prompt user to enter amount for accommodation
6. Prompt user to enter amount for food
7. Add gas + accommodation + food to get total expenses
8. Subtract total expenses from budget to get remaining balance
9. Display travel expense summary:
      - Destination
      - Initial Budget
      - Fuel cost
      - Accommodation cost
      - Food cost
      - Remaining balance
"""


print("This program calculates and displays travel expenses\n")

# Inputs
budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accomodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

# Calculate
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget:.0f}\n")
print(f"Fuel: {gas:.0f}")
print(f"Accomodation: {accommodation:.0f}")
print(f"Food: {food:.0f}\n")
print(f"Remaining Balance: {remaining_balance:.0f}")