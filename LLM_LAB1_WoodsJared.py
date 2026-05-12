# Jared Woods
# Date
# Trivia Game (Randomized Questions)
# This program stores 10 trivia questions, randomly selects questions for the user,
# and allows replay with different questions each time.

import random

# Pseudocode:
# 1. Create a list of questions and answers
# 2. Start a loop to allow replay
# 3. Shuffle or randomly pick questions
# 4. Ask 3 random questions (no repeats)
# 5. Check answers and keep score
# 6. Display score
# 7. Ask user if they want to play again

# List of questions (question, answer)
questions = [
    ("What planet is known as the Red Planet?", "mars"),
    ("How many continents are there on Earth?", "7"),
    ("What is the largest ocean on Earth?", "pacific"),
    ("Who wrote 'Romeo and Juliet'?", "shakespeare"),
    ("What is the capital of the United States?", "washington"),
    ("What gas do plants absorb from the atmosphere?", "carbon dioxide"),
    ("What is 5 + 7?", "12"),
    ("What is the freezing point of water in Celsius?", "0"),
    ("What is the fastest land animal?", "cheetah"),
    ("What is the largest mammal?", "blue whale")
]

play_again = "yes"

while play_again.lower() == "yes":
    score = 0
    print("\nWelcome to the Trivia Game!")
    
    # Randomly select 3 unique questions
    selected_questions = random.sample(questions, 3)

    for i, (question, correct_answer) in enumerate(selected_questions, start=1):
        user_answer = input(f"\n{i}. {question} ")

        if user_answer.lower() == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    print(f"\nYour final score is: {score} out of 3")

    play_again = input("\nDo you want to play again? (yes/no): ")

print("\nThanks for playing!")
