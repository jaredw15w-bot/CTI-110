# Jared Woods
# 04/26/2026
# P5LAB Self-Checkout Simulation
# This program simulates a self-checkout system by generating a random total,
# accepting user payment, calculating change, and displaying the breakdown
# of dollars and coins using a function.

import random

# Function to break down change into coins/bills
def disperse_change(change):
    # Convert to cents to avoid float issues
    change = int(round(change * 100))

    dollars = change // 100
    change = change % 100

    quarters = change // 25
    change = change % 25

    dimes = change // 10
    change = change % 10

    nickels = change // 5
    change = change % 5

    pennies = change

    # Display results (only if greater than 0)
    print()
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")


# Main function
def main():
    # Generate random amount owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")

    # Get user input
    cash = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change
    change = round(cash - total_owed, 2)
    print(f"Change is: ${change:.2f}")

    # Call function
    disperse_change(change)


# Call main
main()