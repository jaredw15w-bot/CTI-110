# Jared Woods
# March 2026
# P1HW Circle Calculations
# This program asks the user for the radius of a circle and calculatesthe diameter, circumference, and area using standard circle formulas.


import math

# Ask user for radius
radius = float(input("What is the radius of the circle? "))

# Perform calculations
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display results with required formatting
print()
print(f"The diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circumference:.2f}")
print()
print(f"The area of the circle is {area:.3f}")