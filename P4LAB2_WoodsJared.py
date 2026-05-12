# Jared Woods
# 5 April 2026
# Assignment Name: P4HW1 - Multiplication Table with Loops
# This program asks the user for an integer and displays
# a multiplication table from 1 to 12.
# The program repeats until the user chooses to stop.

# PSEUDOCODE
# Start program
# Set run_again to "yes"
# While user wants to continue:
#     Ask user for an integer
#     If integer is negative:
#         Display error message
#     Else:
#         Use for loop to display multiplication table 1 through 12
#     Ask user if they want to run again
# End program

run_again = "yes"

# While loop to repeat program
while run_again == "yes":

    number = int(input("Enter an integer: "))

    # Check for negative number
    if number < 0:
        print("This program does not handle negative number!")

    else:
        # For loop for multiplication table
        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")

    print()
    run_again = input("Would you like to run the program again? ").lower()

print("Exiting program...")
