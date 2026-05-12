# Jared Woods
# 04/12/2026
# P4HW1 - Score List and Grade
# This program asks the user how many scores they want to enter,
# validates each score, stores valid scores in a list, drops the
# lowest score, calculates the average, and displays the letter grade.

"""
Pseudocode / Algorithm

1. Create an empty list to store scores.
2. Ask the user how many scores they want to enter.
3. Use a loop to collect that many scores.
4. For each score entered:
   a. Check if the score is between 0 and 100.
   b. If not valid, display an error message.
   c. Keep asking for that same score again until a valid score is entered.
   d. Once valid, add the score to the score list.
5. Find the lowest score in the list.
6. Remove the lowest score from a copy of the list.
7. Calculate the average of the modified list.
8. Determine the letter grade based on the average:
   - A = 90 to 100
   - B = 80 to 89
   - C = 70 to 79
   - D = 60 to 69
   - F = below 60
9. Display:
   - Lowest score
   - Modified list
   - Average
   - Letter grade
"""

# Create empty list
score_list = []

# Ask user for number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Loop to collect scores
for i in range(1, num_scores + 1):
    score = float(input(f"\nEnter score #{i}: "))

    # Validate score
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))

    # Add valid score to list
    score_list.append(score)

# Find and remove lowest score
lowest_score = min(score_list)
modified_list = score_list.copy()
modified_list.remove(lowest_score)

# Calculate average
average_score = sum(modified_list) / len(modified_list)

# Determine letter grade
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print("\n")
print("------------Results------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {modified_list}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {letter_grade}")
print("--------------------------------")
