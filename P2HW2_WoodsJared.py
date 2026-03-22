# Jared Woods
# 03/08/2026
# P2HW2 - Module Grade Analyzer
# This program collects grades for six modules, stores them in a list,
# and displays the lowest grade, highest grade, sum, and average.

"""
Pseudocode 

1. Create an empty list called module_grades
2. Ask the user to enter the grade for Module 1
3. Convert the input to float and add it to the list
4. Repeat the process for Modules 2 through 6
5. Find the lowest grade in the list
6. Find the highest grade in the list
7. Find the sum of all grades in the list
8. Calculate the average grade by dividing the sum by the number of grades
"""

# Create list
module_grades = []

# Collect grades
module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))

# Calculations
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
grade_sum = sum(module_grades)
average = grade_sum / len(module_grades)

# Output results
print("\n------------Results------------")
print(f"Lowest Grade:       {lowest_grade}")
print(f"Highest Grade:      {highest_grade}")
print(f"Sum of Grades:      {grade_sum}")
print(f"Average:            {average:.2f}")
print("--------------------------------")
