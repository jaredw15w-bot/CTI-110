# Jared Woods
# March 2026
# P2LAB2 - Dictionary MPG Calculator
# This program stores vehicle MPG values in a dictionary, allows the user to choose a vehicle, and calculates how many gallons of gas are needed
# to drive a specified number of miles.

# Create dictionary
cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26,
    "Civic": 36,
    "Corolla": 34,
    "Mustang": 24,
    "F-150": 22,
    "RAV4": 30,
    "Accord": 33,
    "Charger": 23,
    "Explorer": 27
}

# Store keys in a variable
keys = cars.keys()

# Print available vehicles
print(keys)
print()

# Ask user to choose a vehicle
vehicle = input("Enter a vehicle to see it's mpg: ")

# Display MPG for selected vehicle
mpg = cars[vehicle]
print()
print(f"The {vehicle} gets {mpg} mpg.")
print()

# Ask user for miles
miles = float(input(f"How many miles will you drive the {vehicle}? "))

# Calculate gallons needed
gallons = miles / mpg

# Display result
print()
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
