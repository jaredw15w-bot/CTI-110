# Jared Woods
# 04/12/2026
# P4HW2
# This program calculates pay for multiple employees, including overtime,
# and displays totals for overtime pay, regular pay, gross pay, and number
# of employees entered.

"""
Pseudocode / Algorithm

1. Set total overtime pay, total regular pay, total gross pay, and employee count to 0.
2. Ask the user to enter an employee name or "Done" to terminate.
3. Use a while loop that continues until the user enters "Done".
4. For each employee:
   a. Ask for hours worked.
   b. Ask for pay rate.
   c. If hours worked is over 40:
      - Calculate overtime hours as hours worked - 40
      - Calculate regular pay for 40 hours
      - Calculate overtime pay as overtime hours * pay rate * 1.5
   d. Otherwise:
      - Overtime hours = 0
      - Overtime pay = 0
      - Regular pay = hours worked * pay rate
   e. Calculate gross pay = regular pay + overtime pay
   f. Display the employee's pay information
   g. Add overtime pay, regular pay, and gross pay to running totals
   h. Increase employee count by 1
   i. Ask for the next employee name or "Done"
5. After the loop ends, display:
   - Total number of employees entered
   - Total amount paid for overtime
   - Total amount paid for regular hours
   - Total amount paid in gross
"""

# Initialize totals
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
employee_count = 0

# Ask for first employee
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Sentinel-controlled loop
while employee_name != "Done":
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Calculate overtime and regular pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    # Display employee results
    print()
    print(f"Employee name:   {employee_name}")
    print()
    print("Hours Worked   Pay Rate    OverTime    OverTime Pay      RegHour Pay       Gross Pay")
    print("--------------------------------------------------------------------------------------")
    print(f"{hours_worked:<14.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<18.2f}${regular_pay:<17.2f}${gross_pay:.2f}")
    print()

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Ask for next employee
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Display totals
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
